from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot

def Questions_Ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton("Дорого"))
    markup.row(InlineKeyboardButton("Качество"))
    markup.row(InlineKeyboardButton("Не Вовремя"))
    markup.row(InlineKeyboardButton('Menu'),InlineKeyboardButton('🔙 Orqaga '))
    return markup