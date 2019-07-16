
import pyodbc
import pandas as pd
from openpyxl import Workbook
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,KeyboardButton,InlineKeyboardMarkup
#from flask import Flask,request
#import os
# Buttons and Keyboards (UZ)
from components.Uz.Main_frame_Uz import Main_Uz
#from components.Uz.Services_Uz import Services_Uz,Tickets
from components.Uz.Info_Uz import Info_Uz
from components.Uz.settings_Uz import Settings_Uz
#from components.Uz.Transport_Uz import Transport_Uz
from components.Language import Language
from components.Uz.Rate_Uz import Rate_Uz
from components.Uz.Countries import Countries_Uz

# Button and Keyboards (RU)
from components.Ru.Main_frame_Ru import Main_Ru
from components.Ru.Services_Ru import Services_Ru
from components.Ru.Info_Ru import Info_Ru
from components.Ru.settings_Ru import Settings_Ru
#from components.Ru.Transport_Ru import Transport_Ru
#from components.Language import Language
from components.Uz.Order_uz import Order_Uz
from components.Ru.Rate_Ru import Rate_Ru
from components.Ru.Questions import Questions_Ru
from components.Uz.Questions_Uz import Questions_Uz
from components.config import Token
import mysql.connector
from mysql.connector import Error
import time

#server = Flask(__name__)



bot = telebot.TeleBot(Token.TOKEN)
user_dict = {"name":"None","phone":"None","chat_id":"None","tg_name":"None","Info_Rate":"None"}
isUz = True
isRu = True
isRegistered = None




@bot.message_handler(commands=['start'])
def Starter(message):
    chat_id = message.chat.id
    try:
        global vote1
        global vote2
        global vote3
        reply_markup = InlineKeyboardMarkup()
        reply_markup.row(InlineKeyboardButton('👍 '+str(vote1),callback_data=f"vote1"),InlineKeyboardButton('❤️ '+str(vote2),callback_data=f"vote2"),InlineKeyboardButton('😎 '+str(vote3),callback_data=f"vote3"))
        bot.send_message(chat_id,'hey here is something interesting!',reply_markup=reply_markup)
        

        print(message.from_user.username)
        bot.disable_save_next_step_handlers()
        bot.send_message(chat_id,"""ColibriSoft xizmat botiga Xush Kelibsiz \n Добро пожаловать на сервис бот ColibriSoft""")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ColibriSoftBot"
        )
        mycursor = mydb.cursor()
        chat_id = message.chat.id
        sql = """ SELECT * FROM users WHERE chat_id="""+str(chat_id)
        mycursor.execute(sql)
        msg = mycursor.fetchone()
        if not msg:
            bot.disable_save_next_step_handlers()
            bot.send_message(chat_id,'Tilni Tanlang || Выберите Язык',reply_markup=Language())
        else:
            global isRegistered
            isRegistered = True
            if isUz:
                Main_Page_handler_Uz(message)
            elif isRu:
                Main_Page_handler_Ru(message)
    except Error as e :
        bot.send_message(chat_id,'ooops')

@bot.callback_query_handler(func=lambda call:True)
def ordering_uz(call):
        bot.answer_callback_query(call.id, "Buyurtmanigiz qabul qilindi...")
        if isRegistered:
            print('reg')
            Fetch_Reg(call.message)
        else:
            print('db')
            Insert_Data_DB(call.message)
    if call.data == "ordering_ru":
        #print(call.message.text)
        bot.answer_callback_query(call.id, "Ваш заказ принят...")
        if isRegistered:
            Fetch_Reg(call.message)
        else:
            Insert_Data_DB(call.message)

###############################Registration###############################################
@bot.message_handler(func=lambda mess: "UZ" == mess.text, content_types=['text'])
def Ask_Name_Uz(message):
    chat_id = message.chat.id
    try:
        isRu = False
        msg = bot.reply_to(message,"""Ismingizni kiriting...""")
        if msg.text.isdigit():
            msg = bot.reply_to(message, 'Ismingiz noto\'g\'ri kiritildi......')
            bot.register_next_step_handler(msg, Ask_Name_Uz)
        bot.register_next_step_handler(message,Ask_ID_Uz)
    except Exception as e:
        bot.send_message(chat_id,'ooops')

@bot.message_handler(func=lambda mess: "RU" == mess.text, content_types=['text'])
def Ask_Name_Ru(message):
    try:
        isUz = False
        chat_id = message.chat.id
        msg = bot.reply_to(message,"""Введите ваше имя: """)
        if msg.text.isdigit():
            msg = bot.reply_to(message, 'Имя введено неккоректно...')
            bot.register_next_step_handler(msg, Ask_Name_Ru)
        bot.register_next_step_handler(msg, Ask_ID_Ru)
    except Exception as e:
        bot.send_message(chat_id,'ooops')

def Ask_ID_Ru(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user_dict["name"] = name
        msg = bot.reply_to(message, 'Введите ваш номер: ')
        bot.register_next_step_handler(msg, Ask_Phone_Ru)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def Ask_ID_Uz(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user_dict["name"] = name
        msg = bot.reply_to(message, 'Raqamingizni kiritng: ')
        bot.register_next_step_handler(msg, Ask_Phone_Uz)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def Ask_Phone_Ru(message):
    chat_id = message.chat.id
    try:
        phone = message.text
        if not phone.isdigit():
            msg = bot.reply_to(message, 'Номер набран некорректно...')
            bot.register_next_step_handler(msg, Ask_Phone_Ru)
            return
        user_dict["chat_id"] = message.chat.id
        user_dict["phone"] = phone
        markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.add(InlineKeyboardButton('Основное Меню'))
        bot.send_message(chat_id,'Регистрация прошла успешна',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def Ask_Phone_Uz(message):
    chat_id = message.chat.id
    try:
        phone = message.text
        if not phone.isdigit():
            msg = bot.reply_to(message, 'Raqam no\'to\'ri kiritildi...')
            bot.register_next_step_handler(msg, Ask_Phone_Uz)
            return
        user_dict["chat_id"] = message.chat.id
        user_dict["phone"] = phone
        user_dict["tg_name"] = message.from_user.username
        markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.add(InlineKeyboardButton('AsosiyMenu'))
        Insert_User(message)
        bot.send_message(chat_id,'Ro\'yxatdan muvaffaqiyatli o\'tdingiz',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Asosiy Menu" == mess.text, content_types=['text'])
def Main_Page_handler_Uz(message):
    try:
        isUz = True
        #bot.disable_save_next_step_handlers()
        chat_id = message.chat.id
        print(user_dict)
        markup = InlineKeyboardMarkup()
        #markup.add(InlineKeyboardButton('Dispetcher',url="https://t.me/FUTBOLTV"))
        #bot.send_message(chat_id,'Dispetcherga ulanish',reply_markup=markup)
        bot.send_message(chat_id,'Asosiy Menu',reply_markup=Main_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)
################################Main Menu###############################################
@bot.message_handler(func=lambda mess: "Основное Меню" == mess.text, content_types=['text'])
def Main_Page_handler_Ru(message):
    try:
        isRu = True
        #bot.disable_save_next_step_handlers()
        chat_id = message.chat.id
        print(user_dict)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Диспетчер',url="https://t.me/FUTBOLTV"))
        bot.send_message(chat_id,'Связаться с Диспетчером',reply_markup=markup)
        bot.send_message(chat_id,'Основное Меню',reply_markup=Main_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')
################################Categories###############################################
@bot.message_handler(func=lambda mess: "Biletlar" == mess.text, content_types=['text'])
def Service_handler_Uz(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Barcha Biletlar:',reply_markup=Services_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Сервисы" == mess.text, content_types=['text'])
def Service_handler_Ru(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Все Сервисы',reply_markup=Services_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "📞 Qo\'ng\'iroq"==mess.text,content_types=['text'])
def Calling(message):
    try:
        chat_id = message.chat.id
        bot.send_contact(chat_id,'998991234567','Kassa')
        bot.send_message(chat_id,'Asosiy Menu',reply_markup=Main_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)

@bot.message_handler(func=lambda mess: "💡 Elektrik" == mess.text, content_types=['text'])
def Elektrik_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо',reply_markup=Services_Uz())
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Elektrik Xizmatlari',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Электрик" == mess.text, content_types=['text'])
def Elektrik_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо:',reply_markup=Services_Ru())
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Сервис Электрика',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔧 Santexnik" == mess.text, content_types=['text'])
def Santexnik_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо',reply_markup=Services_Uz())
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Santexnik Xizmatlari',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Сантехник" == mess.text, content_types=['text'])
def Santexnik_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо',reply_markup=Services_Ru())
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Сервис Сантехника:',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "💻 Programmist" == mess.text, content_types=['text'])
def Programmer_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,"""Web-site va dasturlar xizmati Internet sahiflar va dasturlarga doir istalgan xizmatlaringiz bo’lsa, biz bilan bog’lanishingiz mumkin.""",reply_markup=Services_Uz())
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Programmist Xizmatlari',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Программист" == mess.text, content_types=['text'])
def Programmer_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо',reply_markup=Services_Ru())
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Сервис Программист:',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔧 Barcha Biletlar" == mess.text, content_types=['text'])
def Translator_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,"""• V.I.P. chiptasi Narxi: 200 000 so\'m \n • Oldi Qator chiptasi Narxi: 150 000 so\'m \n • O\'rta qator Narxi: 100 000 so'm """,reply_markup=Services_Uz())
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Barcha Chiptalar:',reply_markup=markup)
        bot.send_message(chat_id,'Tanlang:',reply_markup=Tickets())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Переводчик" == mess.text, content_types=['text'])
def Translator_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо',reply_markup=Services_Ru())
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Сервис Переводчика',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🎛 Payvandlovchi" == mess.text, content_types=['text'])
def Welder_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо',reply_markup=Services_Uz())
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Payvandlovchi Xizmatlari:',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Сварщик" == mess.text, content_types=['text'])
def Welder_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,'Инфо:',reply_markup=Services_Ru())
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Сервис Сварщика',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙 Orqaga" == mess.text, content_types=['text'])
def Back1_handler_Uz(message):
    try:
        Main_Page_handler_Uz(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙Orqaga" == mess.text, content_types=['text'])
def Back2_handler_Uz(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Barcha Xizmatlar:',reply_markup=Services_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙Orqaga " == mess.text, content_types=['text'])
def Back3_handler_Uz(message):
    try:
        Main_Page_handler_Uz(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙 orqaga" == mess.text, content_types=['text'])
def Back4_handler_Uz(message):
    try:
        Settings_handler_Uz(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')

################################Transport###############################################
@bot.message_handler(func=lambda mess: "🚛 Transport" == mess.text, content_types=['text'])
def Transport_service_handler_Uz(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,"""Yuklaringizni boshqa manzilga eltish kerakmi? \n Pochtadan xat va shu kabi narsalarni yubormoqchimisiz? \n Unda quyidagi xizmatlardan foydalanishingiz mumkin:""")
        bot.send_message(chat_id,'Barcha Transport Xizmatlari:',reply_markup=Transport_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Транспорт" == mess.text, content_types=['text'])
def Transport_service_handler_Ru(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Все Сервисы Транспорта:',reply_markup=Transport_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Yetkazish" == mess.text, content_types=['text'])
def Delivery_service_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        bot.send_message(chat_id,"""Unda quyidagi xizmatlardan foydalanishingiz mumkin: \n  
        •	Gul eltib berish; \n
        •	Ovqat tashish; \n
        •	Hujjat eltib berish; \n
        •	Sovg’alarni eltib berish; \n
        •	Va boshqa kuryer xizmati.""",reply_markup=Transport_Uz())
        markup.add(InlineKeyboardButton('Buyurtma berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Yetkazish Transport Xizmati',reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Перевозчик" == mess.text, content_types=['text'])
def Delivery_service_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Транспортный Сервис Перевозки',reply_markup=markup)
        bot.send_message(chat_id,'Инфо:',reply_markup=Transport_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Evakuator" == mess.text, content_types=['text'])
def Evacuator_service_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Evakuator Transport Xizmati',reply_markup=markup)
        chat_id = message.chat.id
        bot.send_message(chat_id,'Инфо:',reply_markup=Transport_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Эвакуатор" == mess.text, content_types=['text'])
def Evacuator_service_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Транспортный Сервис Эвакуатора',reply_markup=markup)
        chat_id = message.chat.id
        bot.send_message(chat_id,'Инфо:',reply_markup=Transport_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Yuk tashuvchi" == mess.text, content_types=['text'])
def Cargo_service_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Yuk tashuvchi Transport Xizmati:',reply_markup=markup)
        chat_id = message.chat.id
        bot.send_message(chat_id,'Инфо',reply_markup=Transport_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Грузовики" == mess.text, content_types=['text'])
def Cargo_service_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Транспортный Сервис Грузовика',reply_markup=markup)
        chat_id = message.chat.id
        bot.send_message(chat_id,'Инфо:',reply_markup=Transport_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Og\'ir texnika" == mess.text, content_types=['text'])
def Heavy_service_handler_Uz(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma berish',callback_data=f"ordering_uz"))
        bot.send_message(chat_id,'Og\'ir texnika Transport Xizmati',reply_markup=markup)
        chat_id = message.chat.id
        bot.send_message(chat_id,'Инфо:',reply_markup=Transport_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Тяжелая техника" == mess.text, content_types=['text'])
def Heavy_service_handler_Ru(message):
    try:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering_ru"))
        bot.send_message(chat_id,'Сервис Тяжелой техники',reply_markup=markup)
        chat_id = message.chat.id
        bot.send_message(chat_id,'Инфо :',reply_markup=Transport_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(func= lambda mess: "ℹ️ Ma\'lumotlar" == mess.text,content_types=['text'])
def Info_Uz_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'“Bilet Express” – bu xohlagan davlatingizdan chipta buyurtma berish, bizga murojaat qiling va biz sizga istalgan konsertingizni istalgan joyingizga moslab chiptalarni sotamiz.',reply_markup=Info_Uz())
    
################################Settings###############################################
@bot.message_handler(func=lambda mess: "🛠 sozlamalar" == mess.text, content_types=['text'])
def Settings_handler_Uz(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Barcha Sozlamalar:',reply_markup=Settings_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🛠 Настройки" == mess.text, content_types=['text'])
def Settings_handler_Ru(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Все Настройки:',reply_markup=Settings_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "Русский язык" == mess.text, content_types=['text'])
def ChangeToRU_handler_Ru(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'Русский язык',reply_markup=Settings_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "O\'zbek tili" == mess.text, content_types=['text'])
def ChangeToUz_handler_Ru(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,'O\'zbek tili',reply_markup=Settings_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙 Назад" == mess.text, content_types=['text'])
def Back1_handler_Ru(message):
    try:
        Main_Page_handler_Ru(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙Назад" == mess.text, content_types=['text'])
def Back2_handler_Ru(message):
    try:
        Main_Page_handler_Ru(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda mess: "🔙Назад " == mess.text, content_types=['text'])
def Back3_handler_Ru(message):
    try:
        Main_Page_handler_Ru(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')
@bot.message_handler(func=lambda mess: "🔙Назад." == mess.text, content_types=['text'])
def Back4_handler_Ru(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Все Сервисы',reply_markup=Services_Ru())


@bot.message_handler(func=lambda mess: "Изменить номер" == mess.text, content_types=['text'])
def ChangePhone_handler_Ru(message):
    isChange = True
    Ask_Phone_Ru(message)
    phone = message.text
    user_dict["phone"] = phone

@bot.message_handler(func=lambda mess: "Tel. raqamni o\'zgartirish" == mess.text, content_types=['text'])
def ChangePhone_handler_Uz(message):
    isChange = True
    Ask_Phone_Uz(message)
    phone = message.text
    user_dict["phone"] = phone

@bot.message_handler(func=lambda mess: "Orqaga"== mess.text,content_type=['text'])
def Back_Info_Uz(message):
    chat_id = message.chat.id
    Main_Page_handler_Uz(message)


################################CallBacks###############################################
@bot.callback_query_handler(func=lambda call:True)
def Ordering(call):
    if call.data == "ordering_uz":
        #print(call.message.text)
        bot.answer_callback_query(call.id, "Buyurtmanigiz qabul qilindi...")
        if isRegistered:
            print('reg')
            Fetch_Reg(call.message)
        else:
            print('db')
            Insert_Data_DB(call.message)
    if call.data == "ordering_ru":
        #print(call.message.text)
        bot.answer_callback_query(call.id, "Ваш заказ принят...")
        if isRegistered:
            Fetch_Reg(call.message)
        else:
            Insert_Data_DB(call.message)

################################Data Base###############################################
def Insert_Data_DB(message):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ColibriSoftBot"
        )
        chat_id = message.chat.id
        mycursor = mydb.cursor()            
        name = user_dict["name"]
        phone = user_dict["phone"]
        chat_id = user_dict["chat_id"]
        info_rate = user_dict["info_rate"]
        orders = message.text
        tg_name = ""
        if tg_name == None:
            tg_name = "None"
        else:
            tg_name = user_dict["tg_name"]
        sql_insert = """INSERT INTO orders (full_name,order_type,tg_name,user_name,phone,info) VALUES (%s,%s,%s,%s,%s,%s) """
        values = (name,orders,tg_name,chat_id,phone,info_rate)
        mycursor.execute(sql_insert,values)
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
    except Error as e :
        bot.send_message(chat_id,'ooops')
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()
def Fetch_Reg(message):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ColibriSoftBot"
        )
        chat_id = message.chat.id
        mycursor = mydb.cursor()  
        #orders = message.text
        sql_fetch = """SELECT full_name,tg_name,user_name,phone FROM orders WHERE user_name="""+str(chat_id)
        mycursor.execute(sql_fetch)
        fetched = mycursor.fetchall()
        mydb.commit()
        for x in fetched:
            user_dict["name"] = x[0]
            user_dict["tg_name"] = x[1]
            user_dict["chat_id"] = x[2]
            user_dict["phone"] = x[3]
        print('hey1')
        Insert_Data_DB(message)
        print("1 record inserted Reg, ID:", mycursor.lastrowid)
    except Error as e:
        bot.send_message(chat_id,'ooops')
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()
def Insert_User(message):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ColibriSoftBot"
        )
        chat_id = message.chat.id
        mycursor = mydb.cursor()
        name = user_dict["name"]
        phone = user_dict["phone"]
        chat_id = user_dict["chat_id"]
        tg_name = user_dict["tg_name"]
        sql = """INSERT INTO users (full_name,phone,chat_id,tg_name) VALUES (%s,%s,%s,%s) """
        values = (name,phone,chat_id,tg_name)
        mycursor.execute(sql,values)
        mydb.commit()
        print("1 user inserted, ID:", mycursor.lastrowid)
    except Error as e :
        bot.send_message(chat_id,'ooops')
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()

def Update_user(message):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ColibriSoftBot"
        )
        full_name = user_dict["name"]
        chat_id = message.chat.id
        mycursor = mydb.cursor()
        sql = """UPDATE users SET full_name= %s WHERE chat_id="""+str(chat_id)
        values = (full_name)
        mycursor.execute(sql,values)
        mydb.commit()
    except Error as e :
        bot.send_message(chat_id,'ooops')
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()
 
@bot.message_handler(func=lambda mess: "IUT_Admin_IUT" == mess.text, content_types=['text'])
def AdminPage(message):
    try:
        chat_id = message.chat.id
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ColibriSoftBot"
        )
        mycursor = mydb.cursor()
        sql = """SELECT * FROM orders ORDER BY user_name """
        mycursor.execute(sql)
        data = mycursor.fetchall()
        df = pd.read_sql_query(sql,mydb)
        writer = pd.ExcelWriter(r'Orders.xlsx')
        df.to_excel(writer, sheet_name='Orders')
        writer.save()
        file_data = open('./Orders.xlsx', 'rb')
        msg = bot.send_document(chat_id,file_data,disable_notification=True)
        assert msg.message_id
    except Error as e :
        bot.send_message(chat_id,'ooops')
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()
################################---------###############################################
@bot.message_handler(func=lambda mess: "Xizmatni Baholash" == mess.text, content_types=['text'])
def Rate_handler_Uz(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,'Xizmatimizni Baholang:',reply_markup=Rate_Uz())
    try:
        QuestionsRate_Uz(message)
    except Exception as e:
        bot.send_message(chat_id,'ooops')

@bot.message_handler(func=lambda mess: "Оценить Сервис" == mess.text, content_types=['text'])
def Rate_handler_Ru(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Оцените Сервис:',reply_markup=Rate_Ru())


@bot.message_handler(content_types=['location'])
def handle_location(message):
    chat_id = message.chat.id
    Info = "Ism: " + user_dict["name"] + "Tel. Raqam: "+ str(user_dict["phone"]) + "ID: " + str(user_dict["chat_id"])
    #print("{0}, {1}".format(message.location.latitude, message.location.longitude))
    bot.send_message(chat_id,Info)
    bot.send_location(614287348,latitude=message.location.latitude,longitude=message.location.longitude)

@bot.message_handler(func=lambda mess: "Изменить Имя" == mess.text, content_types=['text'])
def ChangeName_Ru(message):
    chat_id = message.chat.id
    try:
        msg = bot.reply_to(message,"""Введите ваше имя...""")
        if msg.text.isdigit():
            msg = bot.reply_to(message, 'Имя Введено некорректно......')
            bot.register_next_step_handler(msg,ChangeName_Ru)
        else:
            user_dict["name"] = msg.text
            bot.register_next_step_handler(message,Assign_Name_Ru)
            bot.register_next_step_handler(message,Settings_handler_Ru)
    except Exception as e:
        bot.send_message(chat_id,'ooops')
def QuestionsRate_Uz(message):
    try:
        chat_id = message.chat.id
        if message.text == '3' or '2' or '1':
            bot.send_message(chat_id,'Bahoingizni izohlang...',reply_markup=Questions_Uz())
        elif message.text != '1' or '2' or '3' or '4' or '5':
            bot.send_message(chat_id,'Izohingizni qoldiring...')
        else:
            user_dict["info_rate"] = str(message.text)
            Insert_Data_DB(message)
    except Exception as e:
        bot.send_message(chat_id,'ooops')

@bot.message_handler(func=lambda mess: "ismni o\'zgartirish" == mess.text, content_types=['text'])
def ChangeName_Uz(message):
    chat_id = message.chat.id
    try:
        msg = bot.reply_to(message,"""Ismingizni kiriting...""")
        if msg.text.isdigit():
            msg = bot.reply_to(message, 'Имя Введено некорректно......')
            bot.register_next_step_handler(msg,ChangeName_Uz)
        bot.register_next_step_handler(msg,Assign_Name_Uz)
        bot.register_next_step_handler(message,Settings_handler_Uz)
    except Exception as e:
        bot.send_message(chat_id,'ooops')

def Assign_Name_Uz(message):
    if message.text.isdigit():
        message = bot.reply_to(message, 'Ismingiz noto\'g\'ri kiritildi......')
        bot.register_next_step_handler(message, Assign_Name_Uz)
    user_dict["name"] = message.text
    Update_user(message)
def Assign_Name_Ru(message):
    if message.text.isdigit():
        message = bot.reply_to(message, 'Имя введено некорректно......')
        bot.register_next_step_handler(message, Assign_Name_Ru)
    user_dict["name"] = message.text
def Assign_Phone(message):
    user_dict["phone"] = message.text


bot.polling(none_stop=True,interval=1)