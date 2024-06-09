#7452238296:AAFnS1SfDT4P-27sZFa2Xoeua3eI3X5NwRQ  - telegram bot api
# IjeVMdCTbK5nRVXvucNIumwIOjBhwqM6 -site kkey

import telebot
import requests


#bot manzili---"https://t.me/holidayword_bot"
TELEGRAM_BOT_TOKEN = '7452238296:AAFnS1SfDT4P-27sZFa2Xoeua3eI3X5NwRQ'
# site apisini yozish kerak CALINDARIFIC_API_KEYga
CALENDARIFIC_API_KEY = 'IjeVMdCTbK5nRVXvucNIumwIOjBhwqM6'


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Men sizga hohlagan davatingizni bayramlari haqida malumot beaman \n misol uchun: /holiday UZ")

@bot.message_handler(commands=['holiday'])
def get_holidays(message):
    try:
        message_text2="Agarda yordam kerak bo'lsa Samandarga yozing :)"
        country_code = message.text.split()[1].upper()
        year = 2024
        url = f'https://calendarific.com/api/v2/holidays?&api_key={CALENDARIFIC_API_KEY}&country={country_code}&year={year}'
        response = requests.get(url)
        data = response.json()
        if 'response' in data and 'holidays' in data['response']:
            holidays = data['response']['holidays']
            if holidays:
                message_text = f'{country_code} kegusi bayramalr royxati\n'
                for holiday in holidays:
                    name = holiday['name']
                    date = holiday['date']['iso']
                    message_text += f'{date}: {name}\n'
                bot.reply_to(message, message_text)
                bot.reply_to(message,message_text2)
            else:
                bot.reply_to(message, "Xato habar jo'natildi")
        else:
            bot.reply_to(message, "Qadaydir xato bor qayta jo'nating")
    except IndexError:
        bot.reply_to(message, 'Iltimos, davlat kodini kiriting. Masalan: /holiday US')
bot.polling()
