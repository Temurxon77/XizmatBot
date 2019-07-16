import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Bots_UZ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Chat bo\'ti'),InlineKeyboardButton('Axborot bo\'ti'))
    markup.row(InlineKeyboardButton('Yordamchi bo\'t'),InlineKeyboardButton('Onlayn do\'kon'))
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙Orqaga'))
    return markup