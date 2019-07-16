import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Mobile_RU():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Android'),InlineKeyboardButton('IOS'))
    markup.row(InlineKeyboardButton('React Native(Android&IOS)'),InlineKeyboardButton('Flutter(Android&IOS)'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад.'))
    return markup