# import dependencies

import telebot 
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

def Services_Uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('WEB sayt yaratish'),InlineKeyboardButton('mobil dasturlar yaratish'))
    markup.row(InlineKeyboardButton('Telegram bot yaratish'),InlineKeyboardButton('SMM/SEO'))
    markup.row(InlineKeyboardButton('dizaynerlik ishlari'),InlineKeyboardButton('Kontent menejeri'))
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙Orqaga '))
    return markup
