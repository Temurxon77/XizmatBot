import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def SMM_RU():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Продвижение Социальных страниц'),InlineKeyboardButton('Таргетирование'))
    markup.row(InlineKeyboardButton('Расскрутка сайта'),InlineKeyboardButton('Рекламирования'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад.'))
    return markup