import telebot 
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup


def Countries_Uz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Angliya'),InlineKeyboardButton('Fransiya'),InlineKeyboardButton('O\'zbekiston'))
    return markup