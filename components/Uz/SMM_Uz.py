import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def SMM_UZ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Ijtimoiy tarmoqdagi sahifalar'),InlineKeyboardButton(''))
    markup.row(InlineKeyboardButton('Расскрутка сайта'),InlineKeyboardButton('Рекламирования'))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад.'))
    return markup