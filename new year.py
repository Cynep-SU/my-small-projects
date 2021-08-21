from pygame import mixer # Load the required library
from random import *
import datetime
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
def write_msg(chat_id, message):
    vk.method('messages.send', {'peer_id': chat_id, 'message': message, 'random_id':randint(1,100000000)})
token = "51e76c5d28c63237971eb8a06637cd1397c5b8ff788b5a43a955248e34e7d245d2914dcdf16f6106d4b4a"
vk = vk_api.VkApi(token=token)
quests = ['Крокодил', 'Крокодил', 'За дверью белой небольшой, находится комната холодная-прихолодная, где это там и приз твой', 'Ну что сыграем в футболки', 'Выйди на улицу и крикни "Кукареку"', 'Толстый он стоит в ус не дует', "Слушаем музыку которая тебе нравится", 'Математическая задача',
          'Selfie', 'Быстрый подсчёт', 'Лотерея', 'Лотерея', 'Попейте чаю', 'Съешьте кусок солёной рыбы и запейте сладким соком или лимонадом', "Мясо жарят там сейчас", 'jackbox 5', 'jackbox 5', 'Съешьте кусок солёной рыбы и запейте сладким соком или лимонадом']
vk_id = {}
longpoll = VkBotLongPoll(vk, '164189613')
for i in range(int(input('Kоличество участников игры\n'))):
    a = input('Ваше имя\n')
    print('Напишите боту в вк')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                vk_id.update({a:event.obj.peer_id})
                break
print(vk_id)
times = {}
crocodile = ['Журавль', 'Бегемот', "Чёрт", "Собака", "Кот"]
for el in quests:
    times.update({str(randint(21, 23)) + ':' + str(randint(10, 59)): el})
for el in vk_id:
    write_msg(vk_id[el], 'test')
for el in times:
    write_msg(199720100, el + ' - ' + times[el])
mixer.init()
#mixer.music.load('noti.mp3')
#a = choice(list(vk_id.keys()))
#print(a)
#write_msg(vk_id[a], choice(crocodile))
#mixer.music.play()
while datetime.datetime.now().strftime('%H:%M') != '00:00':
    if datetime.datetime.now().strftime('%H:%M') in times:
        mixer.music.load('noti.mp3')
        mixer.music.play()
        a = choice(list(vk_id.keys()))
        print(times[datetime.datetime.now().strftime('%H:%M')])
        if times[datetime.datetime.now().strftime('%H:%M')] == 'Крокодил':
            print(a)
            write_msg(vk_id[a], choice[crocodile])
        else:
            print(a)
        del times[datetime.datetime.now().strftime('%H:%M')]
print('С новым годым')
