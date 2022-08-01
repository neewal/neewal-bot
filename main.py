import time

import schedule
import telebot
from threading import Thread
from time import sleep

some_id = 735662028
bot = telebot.TeleBot('5385738373:AAG5snmx2XE7A4RSndTBWz68qkTcnud0iWI')
voice1 = 'C:/Users/Night/PycharmProjects/pythonProject/voice/qwerty.mp3'
sticker_url = 'stick/sticker.webp'

def start123():
    print("Загрузка ...")
    time.sleep(3)
    print("2%")
    time.sleep(1)
    print("11%")
    time.sleep(1)
    print("17%")
    time.sleep(1)
    print("29%")
    time.sleep(1)
    print("30%")
    time.sleep(3)
    print("68%")
    time.sleep(1)
    print("81%")
    time.sleep(1)
    print("93%")
    time.sleep(1)
    print("99%")
    time.sleep(7)
    print("100%")
    time.sleep(3)
    print("Bot Скалупопер начал унижать Арсения")
    time.sleep(3)
    print("Я хочу какать!")
    time.sleep(3)
    print("Я цяпля, я цяпля ")
    print('')

print(start123())

# <start>
@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('stick/sticker.webp', 'rb')
    #bot.send_sticker(message.chat.id, sticker)
    text = f'<b>Пошёл нахуй, {message.chat.id}</b>'
    bot.send_message(message.chat.id, text, parse_mode='html')
    photo = open('photo/123.jpg',  'rb')
    bot.send_photo(message.chat.id, photo)
    print('Я ЦАПЛЯ Я ЦАПЛЯ')
# </start>

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


#################### MORN ##################
def good_morning():
    return bot.send_message(some_id, "Долбаёб, вставай, заебал бля. И иди попей водички!")
def gym():
    return bot.send_message(some_id, "Бро, тебе надо тренироваться!")
def eat():
    return bot.send_message(some_id, "Пора кушать жирный аутист")
def shower():
    return bot.send_message(some_id, "БЛя, Чел, от тебя ваняет, иди помойся клОун!")
def water():
    return bot.send_message(some_id, "Иди попей, организм требует воды:)")
#################### MORN ##################

#################### DAY ###################

#################### DAY ###################


############# ((( NAME = MAIN ))) BITCH ##########
if __name__ == "__main__":
    ################# morn ######################
    schedule.every().day.at("10:00").do(good_morning)
    schedule.every().day.at("10:15").do(gym)
    schedule.every().day.at("10:45").do(eat)
    schedule.every().day.at("11:00").do(shower)
    schedule.every().day.at("11:30").do(water)
    ################# morn ######################

    Thread(target=schedule_checker).start()
############# ((( NAME = MAIN ))) BITCH ##########





bot.polling(none_stop=True)