from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot

def Info_Uz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙 Orqaga'))
    return markup
