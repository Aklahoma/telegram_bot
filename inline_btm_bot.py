import telebot
import tokenBot



bot = telebot.TeleBot(tokenBot.token)

@bot.message_handler(content_types=['text'])
def handle_start(message):
    if message.text == '100realty':
        tokenBot.out_text("https://100realty.ua/",message.from_user.id)
    if message.text == 'Parklane':
        tokenBot.out_text('https://parklane.ua/', message.from_user.id)
    if message.text == 'Blagovist':
        tokenBot.out_text('https://blagovist.ua/', message.from_user.id)
    if message.text == 'Bizrealty':
        tokenBot.verify_url_false('https://bizrealty.ua/', message.from_user.id)
    if message.text == 'Bizrealty_UK':
        tokenBot.verify_url_false('https://bizrealty.ua/uk', message.from_user.id)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Клавиатура убрана.', reply_markup=hide_markup)

bot.polling(none_stop=True)