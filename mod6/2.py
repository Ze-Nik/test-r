import requests
from threading import Thread
from datetime import datetime
import time


def get_html(link):
    a = requests.get(link)
    print(a)


data = ['https://www.google.com/', 'https://ya.ru/', 'https://ru.m.wikipedia.org',
        'https://www.youtube.com/','https://www.speedtest.net/']
t1 = datetime.now()
for i in range(len(data)):
    get_html(data[i])
print('последовательный запуск - ', (datetime.now() - t1).microseconds)
t2 = datetime.now()
threads = [Thread(target=get_html, args=(data[i],)) for i in range(5)]
for t in threads:
    t.start()

for t in threads:
    t.join()
print('параллельный запуск - ', (datetime.now() - t2).microseconds)

