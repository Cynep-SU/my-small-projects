from telebot import types
from telebot import apihelper
import re
import json
import threading
import os
import requests
import time
import pickle
from bs4 import BeautifulSoup


url = 'https://henchan.pro/?do=search&subaction=search&story='
dict_ = {}
inline_dict = {}
x = 0
#apihelper.proxy = {'http': 'http://10.10.1.10:3128'}
import telebot


def search(text):
    search = '+'.join(text.split())
    result = requests.get(url + search)
    soup = BeautifulSoup(result.text, 'html.parser')
    apps_list = soup.findAll('h2')
    a = []
    a.append((url + search, f'Ссылка поиска по h-chan по запросу "{search}"'))
    for el in apps_list:
        soup = BeautifulSoup(str(el), 'html.parser')
        b = soup.find('a')
        a.append((b['href'], str(b).split('>')[1][:-3]))
    return a


def save():
    while True:
        try:
            file = open('save.pkl', 'rb')
            a = pickle.load(file)
            file.close()
            file = open('save.pkl', 'wb')
            a.update(inline_dict)
            pickle.dump(a, file, 2)
            file.close()
        except:
            file = open('save.pkl', 'wb')
            pickle.dump(inline_dict, file, 2)
            file.close()
        #time.sleep(60)
threadObj = threading.Thread(target=save)
threadObj.start()

bot = telebot.TeleBot('')


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    global dict_
    global x
    #print(query)
    try:
        query.query
    except Except:
        return
    if len(query.query) < 3:
        pass
    else:
        if query.query in dict_:
            send = dict_[query.query]
        else:
            a = search(query.query)
            send = []
            for i in range(len(a)):
                if False:
                #if i != 0:
                    keyboard = types.InlineKeyboardMarkup()
                    url_button = types.InlineKeyboardButton(
                        text="Читать", callback_data=str(i))
                    keyboard.add(url_button)
                    send.append(types.InlineQueryResultArticle(id=str(i), input_message_content=types.InputTextMessageContent(
                        message_text=a[i][1] + ' — ' + a[i][0]), reply_markup=keyboard, title=a[i][1], url=a[i][0]))
                else:
                    send.append(types.InlineQueryResultArticle(id=str(i), input_message_content=types.InputTextMessageContent(
                        message_text=a[i][1] + ' — ' + a[i][0]), title=a[i][1], url=a[i][0]))
            #print(query)
            inline_dict[query.from_user.id] = a
        bot.answer_inline_query(query.id, send)
        dict_[query.query] = send

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global x
    if call.inline_message_id:
        try:
            str_ = inline_dict[call.from_user.id][int(call.data)][0] + '_' + call.from_user.id
        except KeyError:
            try:
                file = open('save.pkl', 'rb')
                a = pickle.load(file)
                #print(a)
                str_ = a[call.from_user.id][int(call.data)][0] + '_' + call.from_user.id
                file.close()
            except:
                str_ = ''
                bot.send_message(call.from_user.id, 'Извините, кнопка, которую вы нажали очень давно использовалось.')
        file = open('1.txt', 'w')
        file.write(str_)
        file.close()


bot.polling()
