from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot

def Questions_Uz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton("Qimmat"))
    markup.row(InlineKeyboardButton("Sifatsiz"))
    markup.row(InlineKeyboardButton("O\'z vaqtida emas"))
    return markup