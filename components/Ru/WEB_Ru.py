import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types


def WEB_RU():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Посадочный Сайт'),InlineKeyboardButton('Сайт-Каталог'))
    markup.row(InlineKeyboardButton('Сайт-визитка'),InlineKeyboardButton('Онлайн Магазин'))
    markup.row(InlineKeyboardButton('Блог'),InlineKeyboardButton('Индивидуальное решение'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад.'))
    return markup