# Start importing
import telebot
from telebot import types 
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

def Main_Uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add(types.InlineKeyboardButton('Xizmatlarimiz',callback_data="services"))
    markup.add(types.InlineKeyboardButton('ℹ️ Ma\'lumotlar',callback_data="info"))
    return markup
