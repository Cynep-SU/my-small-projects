from telebot import types
from telebot import apihelper

import re
import json
import os
import requests

from bs4 import BeautifulSoup
url = 'https://store.steampowered.com/search/?term='
#apihelper.proxy = {'http': 'http://10.10.1.10:3128'}
import telebot


def search(text):
    search = '+'.join(text.split())
    result = requests.get(url + search)
    soup = BeautifulSoup(result.text, 'html.parser')
    apps_list = soup.findAll('a', class_='search_result_row ds_collapse_flag')
    a = []
    for el in apps_list:
        a.append((el['href'], ' '.join((el['href'].split('/')[5].split('_')))))
    return a


bot = telebot.TeleBot('')


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    if len(query.query) < 3:
        pass
    else:
        a = search(query.query)
        send = []
        for i in range(len(a)):
            send.append(types.InlineQueryResultArticle(id=str(i), input_message_content=types.InputTextMessageContent(
                message_text=a[i][0]), title=a[i][1], url=a[i][0]))
        bot.answer_inline_query(query.id, send)


bot.polling()
