# import dependencies

import telebot 
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

def Services_Ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Разработка Веб-Сайтов'),InlineKeyboardButton('Разработка Мобильных приложених'))
    markup.row(InlineKeyboardButton('Разработка Телеграм ботов'),InlineKeyboardButton('SMM/SEO'))
    markup.row(InlineKeyboardButton('Дизайнерские работы'),InlineKeyboardButton('Контент Менеджмент'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙 Назад'))
    return markup