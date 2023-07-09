import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
    time.sleep(1)
    print(f'{thread_name}')


t1 = datetime.now()
for i in range(5):
    get_thread(i + 1)
print('последовательный запуск - ', (datetime.now() - t1).microseconds)
t2 = datetime.now()
threads = [Thread(target=get_thread, args=(i + 1, )) for i in range(5)]
for t in threads:
    t.start()

for t in threads:
    t.join()
print('параллельный запуск - ', (datetime.now() - t2).microseconds)