import telebot
import requests


bot = telebot.TeleBot("651590241:AAHgKPJL_pkRMPUzMdW9uT-FIrhwTzfgyeM")


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    user_markup.row('/start')
    bot.send_message(message.from_user.id, 'Hello' , reply_markup = user_markup)

@bot.message_handler(commands=['start1'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/start1')
    bot.send_message(message.from_user.id, 'Hello1' , reply_markup = user_markup)

@bot.message_handler(commands=['text'])
def handle_text(message):
    if message.text == 'Test':
        bot.send_message(message.from_user.id, '1')
    if message.text == 'Test1':
        bot.send_message(message.from_user.id, '2')

bot.polling(none_stop=True)