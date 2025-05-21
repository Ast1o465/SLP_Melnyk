import telebot 
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('API_KEY')

config_dict = get_default_config()
config_dict['language'] = 'ua' 
owm = OWM( '0f8480e94c08f6fa663ead777cd2ee53', config_dict  )

@bot.message_handler(commands=['start']) #реакція чат бота на стартову команду
def start_message(message):
    bot.send_message(message.chat.id, 'Ваше повідомлення /start')

@bot.message_handler(commands=['city']) #команда для отримання початкових даних
def cmd_city(message):
    send = bot.send_message(message.chat.id, 'Введи місто')
    bot.register_next_step_handler(send, city)

def city(message): #основна робота з декількома варіантами в залежності від результату
    
    bot.send_message(message.chat.id, 'Дізнаюсь погодні умови в місті {city}'.format(city=message.text))

    data = message.text
    mgr = owm.weather_manager()
    try:

        observation = mgr.weather_at_place(data)
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        t = w.temperature('celsius')['temp']

        answer = f"В місті {message.text} зараз {w.detailed_status} \n"
        answer += f"Приблизна температура {round(t)} ℃\n\n"

        if t < 0:
            answer += 'Зараз температура нижче нуля, одягайся тепліше! 🧣🧤'
            bot.send_animation(message.chat.id, 'https://i.gifer.com/7Fm8.gif')
            
        elif t < 15:
            answer += 'Зараз прохолодно, варто тепліше одягтися! 🧥🌬️' 
            bot.send_animation(message.chat.id, 'https://i.gifer.com/YE52.gif')
            
        else:
            answer += 'Зараз досить тепло, можна одягтися легко! 😎🌞'
            bot.send_animation(message.chat.id, 'https://media1.tenor.com/m/V_zTe0MqPJkAAAAd/%D1%81%D0%B5%D1%80%D0%B5%D0%B3%D0%B0%D0%BF%D0%B8%D1%80%D0%B0%D1%82-%D1%81%D0%B5%D1%80%D0%B5%D0%B3%D0%B0.gif')
    except:
        answer = 'На жаль, я не можу знайти таке місто. Спробуйте ще раз.'
        
        
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True) # необхідно, щоб бот не вимкнувся одразу 