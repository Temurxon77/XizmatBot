import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton
from telebot import types 


def Language():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add(KeyboardButton('RU',request_location=False),KeyboardButton('UZ'))
    return markup