import json
import locale
import time

import requests
import vk_api

locale.setlocale(locale.LC_ALL, '')

vk_session = vk_api.VkApi('', '')
vk_session.auth()
vk = vk_session.get_api()
chat_id = -1001258426469


def send(author, text, photo_url, files):
    url = ""

    embed = {
        "description": text,
        "author": {
            "name": author,
            "icon_url": photo_url
        }

    }
    if len(files) > 0:
        for title, file in files:
            embed['description'] += '\n\n' + f'[{title}]({file})'

    data = {
        "content": "",
        "username": "КРЧ ТАМ В ОБСУЖДЕНИЕ ЧТО-ТО ПРИСЛАЛИ",
        "embeds": [
            embed
        ],
    }

    headers = {
        "Content-Type": "application/json"
    }

    result = requests.post(url, json=data, headers=headers)


while True:
    with open('ignore_id.json', 'r') as file:
        ignore_ids = json.loads(file.read())
    for el in list(reversed(vk.board.getComments(group_id='193019185', topic_id='46388603', count=10,
                                                 sort='desc')['items'])):
        if el['id'] in ignore_ids:
            continue
        get_ = vk.users.get(user_ids=el['from_id'], name_case='Nom', fields='photo_200')
        author = get_[0]['last_name'] + ' ' + get_[0]['first_name']
        files = []
        try:
            for file in el['attachments']:
                files.append((file[file['type']]['title'], file[file['type']]['url'][:file[file['type']]['url'].find('&')]))
        except KeyError:
            pass
        send(author, el['text'], get_[0]["photo_200"], files)
        ignore_ids.append(el['id'])
    with open('ignore_id.json', 'w') as file:
        file.write(json.dumps(ignore_ids))
    time.sleep(300)
