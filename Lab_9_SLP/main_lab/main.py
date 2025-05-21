import nasa
import telebot
from datetime import datetime
from deep_translator import GoogleTranslator

TELEGRAM_TOKEN = 'API_KEY'
NASA_TOKEN = 'API_KEY'

MIN_DATE = datetime(1995, 6, 16).date()

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None

def translate_uk(text):
    try:
        return GoogleTranslator(source='auto', target='uk').translate(text)
    except Exception:
        return text
    
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "<b>🤖 Привіт!</b> Я бот, який надає інформацію про зображення дня NASA.\n"
        "<b>Використовуйте команди:</b>\n"
        "<b>/apod</b> - Отримати зображення дня NASA.\n"
        "<b>/apod ДД.ММ.РРРР</b> - Отримати зображення дня за вказаною датою (не раніше 16.06.1995).\n"
        "<b>/help</b> - Отримати цю довідку."
    )
    bot.send_message(message.chat.id, help_text, parse_mode='HTML')

@bot.message_handler(commands=['apod'])
def send_apod(message):
    parts = message.text.strip().split()
    date = None
    if len(parts) > 1:
        user_date = parse_date(parts[1])
        if not user_date:
            bot.send_message(message.chat.id, "❗ Некоректний формат дати. Використовуйте ДД.ММ.РРРР, наприклад: /apod 01.06.2024")
            return
        if not (MIN_DATE <= user_date <= datetime.now().date()):
            bot.send_message(message.chat.id, f"❗ Дата повинна бути в діапазоні від {MIN_DATE.strftime('%d.%m.%Y')} до {datetime.now().strftime('%d.%m.%Y')}.")
            return
        date = user_date.strftime("%Y-%m-%d")

    apod = nasa.APOD()
    response = apod.apod(NASA_TOKEN, date=date) if date else apod.apod(NASA_TOKEN)
    if callable(getattr(response, "__await__", None)):
        import asyncio
        response = asyncio.run(response)
    if not isinstance(response, dict):
        bot.send_message(message.chat.id, f"Не вдалося отримати відповідь від NASA API.\nВідповідь: {response}")
        return

    media_type = response.get('media_type', 'image')
    url = response.get('url')
    apod_date = response.get('date', '')
    try:
        apod_date_fmt = datetime.strptime(apod_date, "%Y-%m-%d").strftime("%d.%m.%Y")
    except Exception:
        apod_date_fmt = apod_date

    # Переклад title та explanation на українську
    title = response.get('title', '')
    explanation = response.get('explanation', '')
    title_uk = translate_uk(title) if title else ''
    explanation_uk = translate_uk(explanation) if explanation else ''

    caption = f"🌌 {title_uk}\n\n{explanation_uk}\n\n📅 Дата: {apod_date_fmt}"

    if media_type == 'image' and url:
        # Перевіряємо довжину caption
        if len(caption) > 1024:
            short_caption = f"🌌 {title_uk}\n\n📅 Дата: {apod_date_fmt}"
            bot.send_photo(message.chat.id, photo=url, caption=short_caption)
            # Відправляємо пояснення окремо
            bot.send_message(message.chat.id, explanation_uk)
        else:
            bot.send_photo(message.chat.id, photo=url, caption=caption)
    elif media_type == 'video' and url:
        bot.send_message(message.chat.id, f"{caption}\n\n🎬 Відео: {url}")
    else:
        bot.send_message(message.chat.id, f"{caption}\n\n🔗 Медіа: {url or '(Медіа недоступне для перегляду через Telegram)'}")

if __name__ == '__main__':
    bot.polling(none_stop=True)