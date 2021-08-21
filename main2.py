import threading
import time
from datetime import datetime

import psutil
import pyautogui
import requests
import telebot
import vk_api
from bs4 import BeautifulSoup

bot = telebot.TeleBot('')
token = ""
vk = vk_api.VkApi(token=token)


def check_steam(url: str) -> str:
    headers = {"Accept-Language": "ru"}
    get_profile = requests.get(url, headers=headers)
    get_profile.encoding = 'utf-8'
    soup = BeautifulSoup(get_profile.text, 'html.parser')
    mydivs = soup.findAll("div", {"class": "profile_in_game_header"})
    try:
        if mydivs[0].contents[0] != 'В сети':
            mydivs = soup.findAll("div", {"class": "profile_in_game_name"})
        return mydivs[0].contents[0]
    except IndexError:
        return 'В сети'


def check_overwatch() -> bool:
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'Overwatch.exe':
                return True
        except:
            pass
    return False


def check_discord() -> bool:
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'Discord.exe':
                return True
        except:
            pass
    return False


def check_vk():
    return vk.method("users.get",
                     {"user_ids": ["199720100"], "fields": "online, last_seen", "name_case": "Nom"})[
        0]


def working(mes_id, chat_id):
    dots = 2
    while True:
        if dots > 10:
            dots = 1
        try:
            bot.edit_message_text("Наблюдаю за Васей" + dots * ".", chat_id=chat_id,
                                  message_id=mes_id)
        except Exception as e:
            break
        dots += 1


@bot.message_handler(commands=["online"])
def i_online(message):
    mes = bot.send_message(message.chat.id, "Наблюдаю за Васей.").id
    mythread = threading.Thread(target=working, args=(mes, message.chat.id))
    mythread.start()
    req = "Steam = " + check_steam("https://steamcommunity.com/id/Super_Su_Vova_Petrov/")
    m = check_vk()
    print(check_vk())
    req += "\nVK = "
    if m["online"] == 1:
        req += "В сети"
    else:
        req += "был в " + datetime.utcfromtimestamp(m["last_seen"]["time"]).strftime(
            '%H:%M:%S %d-%m-%Y')
    req += "\nНа компьютере открыты:"
    if check_discord():
        req += "\n    Discord"
    if check_overwatch():
        req += "\n    Overwatch"
    if req[-1] == ":":
        req += "\n    Ничего не открыто"
    bot.send_message(message.chat.id, req)
    bot.delete_message(message.chat.id, mes)


@bot.message_handler(commands=["screenshot"])
def screen(message):
    mes = bot.send_message(message.chat.id, "Наблюдаю за Васей.").id
    mythread = threading.Thread(target=working, args=(mes, message.chat.id))
    mythread.start()
    pyautogui.screenshot("123.jpg")
    bot.send_message(message.chat.id, "Скриншот с Васиного компьютера")
    bot.send_photo(message.chat.id, photo=open('123.jpg', 'rb'))
    bot.delete_message(message.chat.id, mes)


@bot.message_handler()
def get_text(message):
    bot.send_message(message.chat.id, "У бота пока есть только две команды /online и /screenshot. "
                                      "А вы ввели что-то не то.")


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
