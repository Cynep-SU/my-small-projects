import vk_api
import time
import psutil
import requests
from bs4 import BeautifulSoup


overwatch = ''
yandex_music = ''
pycharm = ''
# from yandex_music.client import Client

# client = Client.from_credentials('example@yandex.com', 'password')
old_status = ''
old_status_checked = False


def vk_login(login: str, password: str) -> vk_api.vk_api.VkApiMethod:
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk


def change_status(vk: vk_api.vk_api.VkApiMethod, new_status: str) -> dict:
    global old_status, old_status_checked
    if old_status == '' and not old_status_checked:
        old_status = vk.account.getProfileInfo()['status']
        old_status_checked = True
    return vk.account.saveProfileInfo(status=new_status)


def back_status(vk: vk_api.vk_api.VkApiMethod) -> None:
    vk.account.saveProfileInfo(status=old_status)


# def get_yandex_music(login: str, password: str) -> Client:
# return Client.from_credentials(login, password)



def check_yandex_music() -> bool:
    global yandex_music
    if yandex_music != '' and yandex_music in psutil.process_iter():
        return True
    else:
        yandex_music = ''

    for proc in psutil.process_iter():
        try:
            if proc.name() == 'Y.Music.exe':
                yandex_music = proc
                return True
        except:
            pass
    return False


# print(check_yandex_music())
'''for proc in psutil.process_iter():
    try:
        print(proc.name())
    except:
        pass
'''


def check_overwatch() -> bool:
    global overwatch
    if overwatch != '' and overwatch in psutil.process_iter():
        return True
    else:
        overwatch = ''
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'Overwatch.exe':
                return True
        except:
            pass
    return False


def check_pycharm() -> bool:
    global pycharm
    if pycharm != '' and pycharm in psutil.process_iter():
        return True
    else:
        pycharm = ''
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'pycharm64.exe':
                return True
        except:
            pass
    return False


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



def main() -> None:
    vk = vk_login('', '')
    while True:
        steam = check_steam('https://steamcommunity.com/id/CykaBlyatPetrovVova/')
        steam_ = False
        if steam != 'В сети':
            steam_ = True
            steam = 'играет в ' + steam
        yandex_music_ = check_yandex_music()
        overwatch_ = check_overwatch()
        pycharm_ = check_pycharm()
        new_status = ''
        if yandex_music and overwatch_ and pycharm_ and steam_:
            new_status = f'Играет в Overwatch, кодит в pycharm и при этом слушает музыку, a также {steam}'
        elif yandex_music and overwatch_ and pycharm_:
            new_status = 'Играет в Overwatch, кодит в pycharm и при этом слушает музыку'
        elif yandex_music_ and pycharm_ and steam_:
            new_status = f"Кодит в Pycharm, слушает музыку и {steam}"
        elif yandex_music_ and overwatch_ and steam_:
            new_status = f"Играет в Overwatch и слушает музыку, а также {steam}"
        elif yandex_music_ and pycharm_:
            new_status = "Кодит в Pycharm и слушает музыку"
        elif yandex_music_ and overwatch_:
            new_status = "Играет в Overwatch и слушает музыку"
        elif pycharm_:
            new_status = 'Кодит в pycharm'
        elif yandex_music:
            new_status = 'Слушает музыку'
        elif overwatch_:
            new_status = 'Играет в Overwatch'
        elif steam_:
            new_status = steam.title()
        if new_status != '':
            change_status(vk, new_status)
        else:
            back_status(vk)
        time.sleep(15)


main()
