from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from telebot import types
import telebot

def Language():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add(InlineKeyboardButton("RU"),InlineKeyboardButton("UZ"))
    return markup