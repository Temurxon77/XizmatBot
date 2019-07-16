from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot


def Settings_Ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton("O\'zbek tili"),InlineKeyboardButton("Русский язык"))
    markup.row(InlineKeyboardButton("Изменить Имя"),InlineKeyboardButton("Оценить Сервис"))
    markup.row(InlineKeyboardButton('Основное Меню'),InlineKeyboardButton('🔙Назад'))
    return markup
