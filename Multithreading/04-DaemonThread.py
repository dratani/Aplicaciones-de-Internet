import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
def daemon():
    logging.debug('Iniciando')
    time.sleep(2)
    logging.debug('Terminando')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Iniciando')
    logging.debug('Terminando')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

#d.join()
#t.join()