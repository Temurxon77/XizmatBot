from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot


def Settings_Uz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton("O\'zbek tili"),InlineKeyboardButton("Русский язык"))
    markup.row(InlineKeyboardButton("ismni o\'zgartirish"),InlineKeyboardButton("raqamni o\'zgartirish"),InlineKeyboardButton("Xizmatni Baholash"))
    markup.row(InlineKeyboardButton('Asosiy Menu'),InlineKeyboardButton('🔙 Orqaga '))
    return markup
