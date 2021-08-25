import threading
import time


def worker():
    print (threading.currentThread().getName(), 'Iniciando')
    time.sleep(2)
    print (threading.currentThread().getName(), 'Terminando')

def my_service():
    print (threading.currentThread().getName(), 'Iniciando')
    time.sleep(3)
    print (threading.currentThread().getName(), 'Terminando')

t = threading.Thread(name='Servicio 1', target=my_service)
w = threading.Thread(name='Trabajador', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()