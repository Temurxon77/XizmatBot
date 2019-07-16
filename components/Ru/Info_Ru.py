from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot

def Info_Ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton('Вопросы'))
    markup.row(InlineKeyboardButton('Меню'),InlineKeyboardButton('Назад'))
    return markup
