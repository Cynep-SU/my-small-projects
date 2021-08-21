from telebot import types
from telebot import apihelper
import telebot
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import requests
import time
bot = telebot.TeleBot('')

reading_users = {}

def read(url):
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + r'C:\Users\Супер Вася\Desktop\Python\2.0.7_0')
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
    driver.get('https://henchan.pro/')
    elem = driver.find_element_by_name('login_name')
    elem.send_keys('Super login')
    elem = driver.find_element_by_name('login_password')
    elem.send_keys('e44fffdc3ec')
    elem.send_keys(Keys.ENTER)
    driver.get(url)
    elem = driver.find_element_by_id('manga_images')
    elem.click()
    elem = driver.find_element_by_class_name('thumb')
    elem.click()
    elem = driver.find_element_by_id('image')
    html = ''
    while html == '':
        html = str(elem.get_attribute('innerHTML'))
        a = html[html.find('https'): html.find('"></a><img src=')]
        #print(html)
    driver.close()
    return a
    # time.sleep(60)

def next_page(url):
    num_page = int(url[-6])
    if url[-7].isalnum() and url[-7] != '0':
        num_page += 10 * int(url[-7])
        a = list(url)
        del a[-7]
    elif str(num_page)[-1] == '9' and num_page < 10 and not url[-7].isalnum():
        a = list(url)
    elif str(num_page)[-1] == '9' and num_page < 10:
        a = list(url)
        del a[-7]
    else:
        a = list(url)
    a[-6] = str(num_page + 1)
    return ''.join(a), num_page


def back_page(url):
    b = True
    num_page = int(url[-6])
    if url[-7].isalnum() and url[-7] != '0':
        num_page += 10 * int(url[-7])
        if num_page != 10:
            a = list(url)
            del a[-7]
            b = False
    if num_page == 10 and b:
        a = list(url)
        a[-7] = '0'
    elif b:
        a = list(url)
    a[-6] = str(num_page - 1)
    return ''.join(a), num_page

def max_page(start_page):
    start_page = next_page(start_page)
    for i in range(30):
        start_page = next_page(start_page[0])
        response = requests.get(start_page[0])
        if response.status_code != 200:
            #print('Комикс закончился')
            break
        #print(start_page)
    return start_page[1]


def listen():
    while True:
        catolog = os.listdir()
        if '1.txt' in catolog:
            time.sleep(0.01)
            file = open('1.txt', 'r')
            print(file.read())
            file.close()
            os.remove('1.txt')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Этот бот позволяет читать мангу с сайта henchan.pro')
    print(message.chat.id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    # print(message)
    if message.text.lower().startswith('https://henchan.pro/manga/') or message.text.lower().startswith('henchan.pro/manga/'):
        bot.send_message(message.chat.id, 'Подождите в районе минуты.')
        first_photo = read(message.text)
        max_page_ = max_page(first_photo)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="👈", callback_data='1')
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(
            text=f"1/{max_page_}", callback_data='2')
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(
            text="👉", callback_data='3')
        reading_users[message.chat.id] = (message.text, 1)
        print(first_photo)
        bot.send_photo(chat_id=message.chat.id, photo=first_photo)
    else:
        bot.send_message(message.chat.id, 'Это не ссылка на мангу.')
threadObj = threading.Thread(target=listen)
threadObj.start()
bot.polling()
