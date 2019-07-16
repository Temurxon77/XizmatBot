import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Mobile_UZ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Android'),InlineKeyboardButton('IOS'))
    markup.row(InlineKeyboardButton('React Native(Android va IOS)'),InlineKeyboardButton('Flutter(Android va IOS)'))
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙Orqaga'))
    return markup