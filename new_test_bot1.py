import requests
import json



token = "651590241:AAHgKPJL_pkRMPUzMdW9uT-FIrhwTzfgyeM"

bot_url = 'https://api.telegram.org/bot651590241:AAHgKPJL_pkRMPUzMdW9uT-FIrhwTzfgyeM/'



def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_updates():
    URL = bot_url + 'getUpdates'
    r = requests.get(URL)
    write_json(r.json())


def start():
#    r = requests.get(bot_url + 'getMe')
#   write_json(r.json())
    get_updates()



