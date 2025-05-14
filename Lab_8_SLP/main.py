import telebot
import random

bot = telebot.TeleBot('api_token')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '👋 Вітаю! Ваше повідомлення /start')

@bot.message_handler(commands=['coinflip'])
def coinflip_message(message):
    result = random.choice(['🪙 Орел!', '🪙 Решка!'])
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id,
        '🆘 Список команд:\n'
        '/start - почати\n'
        '/help - допомога\n'
        '/hello - привітання\n'
        '/coinflip - підкинути монетку\n'
        '/sticker - надіслати стікер\n'
        '/github - Гітхаб з лабораторними'
    )

@bot.message_handler(commands=['hello'])
def hello_message(message):
    bot.send_message(message.chat.id, 'Привіт! 😊 Як справи?')

@bot.message_handler(commands=['github'])
def github_message(message):
    bot.send_message(message.chat.id, 'GitHub: https://github.com/Ast1o465/SLP_Melnyk')

@bot.message_handler(commands=['sticker'])
def sticker_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPGBtoJLdCxoGY3VE56zpDvaTkw4AHqwACJBYAAsnI-Uiwgeatgm5yiDYE')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.strip().lower()
    if text == 'цнту' or text == 'cntu':
        bot.send_message(message.chat.id, 'Офіційний сайт ЦНТУ: https://www.kntu.kr.ua/')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPGCVoJLjhxpOF6ddpTbEwTDAT183xXgACLhMAAvMMiUgV--qnbKiCHjYE')

    elif text == 'потужність на максимумі':
        bot.send_photo(
            message.chat.id,
            'https://www.radiosvoboda.org/a/news-zelensky-ssha-dopomoha-aktyvy-rosii/33235217.html',  # замініть на своє посилання або file_id, якщо потрібно інше фото
            caption='ПОТУЖНІСТЬ НА МАКСИМУМІ! 💪'
        )
    elif text == 'дота' or text == 'dota' or text == 'дота 2' or text == 'dota 2':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPGD1oJMA8PlK52wtNSUqarmTxnrVpTAACMxEAAgTFAAFLVRSRDqRP0VY2BA')
        bot.send_photo(
            message.chat.id, 'http://pdd.com.ua/ru/33/2.2/'
        )

    elif text == 'ЦДУ' or text == 'цду' or text == 'ЦДПУ' or text == 'цдпу':
        bot.send_message(message.chat.id, 'Центральноукраїнський державний педагогічний університет імені Володимира Винниченка')
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')


bot.polling(none_stop=True)
