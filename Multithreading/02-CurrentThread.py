import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="[%(threadName)-10s] %(message)s")
def worker():
    print (threading.currentThread().name, 'Iniciando')
    logging.debug("Iniciando")
    time.sleep(2)
    logging.debug("Terminando")
 #   print (threading.currentThread().name, 'Terminando')

def my_service():
  #  print (threading.currentThread().name, 'Iniciando')
    logging.debug("Iniciando")
    time.sleep(3)
  #  print (threading.currentThread().name, 'Terminando')
    logging.debug("Terminando")

t = threading.Thread(name='Servicio 1', target=my_service)
w = threading.Thread(name='Trabajador', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()