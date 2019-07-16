import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Content_UZ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Saytni ma\'lumot bilan to\'ldirish'),InlineKeyboardButton('CopyWriting'))
    markup.row(InlineKeyboardButton('Sayt bilan ishlash'))
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙Orqaga'))
    return markup