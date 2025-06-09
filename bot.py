import telebot
from telebot import types
import os
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
users = {}
waiting_list = []
pairs = {}
