from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
import telebot

def Ordering():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Buyurtma berish',callback_data=f"order"))
    return markup