import telebot
import requests
import time
import hashing

bot = telebot.TeleBot(hashing.token)

@bot.message_handler(commands=['newbtn'])
def handle_start(message):
    newbtn = telebot.types.InlineKeyboardButton(text='Test1', callback_data=1)
    bot.send_message(message.from_user.id, 'Bla')


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('https://100realty.ua/', 'https://parklane.ua/', 'https://blagovist.ua/')
    user_markup.row('https://bizrealty.ua/', 'https://frg.ua/')
    bot.send_message(message.from_user.id, 'Выберите сайт:', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_start(message):
    if (message.text.find("http://") != -1 or message.text.find("https://") != -1):
        if message.text.find("bizrealty") != -1:
            verify_url_false(message.text, message.from_user.id)
        else:
            out_text(message.text, message.from_user.id)
    else:
        bot.send_message(message.from_user.id, 'Введите адресс сайта: напр. <a href="https://www.google.com/">https://google.com</a>.', disable_web_page_preview=True, parse_mode="HTML")



def out_text(url, id):
    t1 = int(round(time.time() * 1000))
    r = requests.get(url)
    t2 = int(round(time.time() * 1000))
    status = '<b>Status code</b>: ' + str(r.status_code)
    time_load = str((t2 - t1) / 1000)
    sec = '\nLoadtime: ' + time_load + 's'
    bot.send_message(id, url +"\n"+ status + sec, disable_web_page_preview=True, parse_mode='HTML')

def verify_url_false(url, id):
    t1 = int(round(time.time() * 1000))
    r = requests.get(url, verify=False)
    t2 = int(round(time.time() * 1000))
    status = '<b>Status code</b>: ' + str(r.status_code)
    time_load = str((t2 - t1) / 1000)
    sec = '\nLoadtime: ' + time_load + 's'
    bot.send_message(id, url + "\n" + status + sec, disable_web_page_preview=True, parse_mode='HTML')

bot.polling(none_stop=True)