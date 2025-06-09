import telebot
from telebot import types

TOKEN = 'ТВОЙ_ТОКЕН'  # встав сюди свій токен
bot = telebot.TeleBot(TOKEN)
users = {}
waiting_list = []
pairs = {}
