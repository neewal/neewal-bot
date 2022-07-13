import telebot

bot = telebot.TeleBot('5385738373:AAG5snmx2XE7A4RSndTBWz68qkTcnud0iWI')
voice1 = 'C:/Users/Night/PycharmProjects/pythonProject/voice/qwerty.mp3'
sticker_url = 'stick/sticker.webp'

# <start>
@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('stick/sticker.webp', 'rb')
    #bot.send_sticker(message.chat.id, sticker)
    text = f'<b>Пошёл нахуй, {message.chat.first_name}</b>'
    bot.send_message(message.chat.id, text, parse_mode='html')
    photo = open('photo/123.jpg',  'rb')
    bot.send_photo(message.chat.id, photo)
# </start>


bot.polling(none_stop=True)