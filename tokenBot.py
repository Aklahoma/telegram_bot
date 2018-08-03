import requests
import time


token = "651590241:AAHgKPJL_pkRMPUzMdW9uT-FIrhwTzfgyeM"

#post на url с сертификатом
def out_text(url, id):
    t1 = int(round(time.time() * 1000))
    r = requests.get(url)
    t2 = int(round(time.time() * 1000))
    status = '<b>Status code</b>: ' + str(r.status_code)
    time_load = str((t2 - t1) / 1000)
    sec = '\nLoadtime: ' + time_load + 's'
    bot.send_message(id, url +"\n"+ status + sec, disable_web_page_preview=True, parse_mode='HTML')

#post на url без сертификата
def verify_url_false(url, id):
    t1 = int(round(time.time() * 1000))
    r = requests.get(url, verify=False)
    t2 = int(round(time.time() * 1000))
    status = '<b>Status code</b>: ' + str(r.status_code)
    time_load = str((t2 - t1) / 1000)
    sec = '\nLoadtime: ' + time_load + 's'
    bot.send_message(id, url + "\n" + status + sec, disable_web_page_preview=True, parse_mode='HTML')
