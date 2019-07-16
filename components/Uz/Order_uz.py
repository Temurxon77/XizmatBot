import telebot
from telebot import types 
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

def Order_Uz():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Buyurtma berish',callback_data="order_uz"))
    return markup