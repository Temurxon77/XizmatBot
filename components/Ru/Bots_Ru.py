import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Bots_RU():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Чат-боты'),InlineKeyboardButton('Боты-Информаторы'))
    markup.row(InlineKeyboardButton('Боты-асистенты'),InlineKeyboardButton('Онлайн Магазин'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад.'))
    return markup