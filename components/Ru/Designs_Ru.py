import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Designs_RU():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Рекламные Баннеры'),InlineKeyboardButton('Верстка сайтов'))
    markup.row(InlineKeyboardButton('UI/UX дизайн'),InlineKeyboardButton('Разработка логотипов'))
    markup.row(InlineKeyboardButton('Видеомонтаж'),InlineKeyboardButton('Обучения'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад.'))
    return markup