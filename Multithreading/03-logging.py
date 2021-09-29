import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
def worker():
    logging.debug('Iniciando')
    time.sleep(2)
    logging.debug('Terminando')

def my_service():
    logging.debug('Iniciando')
    time.sleep(3)
    logging.debug('Terminando')

t = threading.Thread(name='Servicio 1', target=my_service)
w = threading.Thread(name='Trabajador', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()