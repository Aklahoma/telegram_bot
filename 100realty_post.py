import requests
import time

t1 = int(round(time.time() * 1000))
r = requests.get("http://bizrealty.ua/", verify=False)
t2 = int(round(time.time() * 1000))
print('Status code:', r.status_code)
print('Loadtime:', ((t2 - t1) / 1000), 's')
