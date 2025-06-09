import telebot
from telebot import types
import os
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
users = {}
waiting_list = []
pairs = {}
if __name__ == "__main__":
    bot.polling(none_stop=True)
