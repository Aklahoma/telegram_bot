import telebot
import tokenBot



bot = telebot.TeleBot(tokenBot.token)
#chat.id = '122404525'
# bot.send_message(122404525, 'test')


# upd = bot.get_updates()
# print(upd)

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)


#@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

#@bot.message_handler(commands=[' stop'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('a')
    itembtnv = types.KeyboardButton('v')
    itembtnc = types.KeyboardButton('c')
    itembtnd = types.KeyboardButton('d')
    itembtne = types.KeyboardButton('e')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

bot.polling(none_stop=True, interval=0)



# or add KeyboardButton one row at a time:
