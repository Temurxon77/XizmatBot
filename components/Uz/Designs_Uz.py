import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Designs_UZ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Reklama banerlari'),InlineKeyboardButton('Sayt dizayni'))
    markup.row(InlineKeyboardButton('UI/UX dizayni'),InlineKeyboardButton('Logotiplar yaratish'))
    markup.row(InlineKeyboardButton('Video Montaj'),InlineKeyboardButton('O\'rgatish'))
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙Orqaga'))
    return markup