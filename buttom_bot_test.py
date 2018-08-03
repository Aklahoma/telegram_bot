import telebot
import requests
import time

bot = telebot.TeleBot("651590241:AAHgKPJL_pkRMPUzMdW9uT-FIrhwTzfgyeM")

@bot.message_handler(commands=['newbtn'])
def handle_start(message):
    newbtn = telebot.types.InlineKeyboardButton(text='Test1', callback_data=1)
    bot.send_message(message.from_user.id, 'Bla')


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('100realty', 'Parklane', 'Blagovist')
    user_markup.row('Bizrealty', 'Bizrealty_UK')
    bot.send_message(message.from_user.id, 'Выберите сайт:', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_start(message):
    if message.text == '100realty':
        out_text("https://100realty.ua/",message.from_user.id)
    if message.text == 'Parklane':
        out_text('https://parklane.ua/', message.from_user.id)
    if message.text == 'Blagovist':
        out_text('https://blagovist.ua/', message.from_user.id)
    if message.text == 'Bizrealty':
        verify_url_false('https://bizrealty.ua/', message.from_user.id)
    if message.text == 'Bizrealty_UK':
        verify_url_false('https://bizrealty.ua/uk', message.from_user.id)

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


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove(True)
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)



bot.polling(none_stop=True)