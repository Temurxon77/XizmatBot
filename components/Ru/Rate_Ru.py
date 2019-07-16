import telebot
from telebot import types 
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

def Rate_Ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add(types.InlineKeyboardButton('1'))
    markup.add(types.InlineKeyboardButton('2'))
    markup.add(types.InlineKeyboardButton('3'))
    markup.add(types.InlineKeyboardButton('4'))
    markup.add(types.InlineKeyboardButton('5'))
    return markup