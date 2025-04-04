import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )


class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.buffer = []
        self.SeccionCritica = threading.Lock()

    def producir(self, ):
        with self.SeccionCritica:
            self.buffer.append("producto")
            logging.debug('Ejecutando producir ')

    def consumir(self, ):
        with self.SeccionCritica:
            self.buffer.remove("producto")
            logging.debug('Ejecutando consumir')


def productor(s, pool):
    logging.debug('Esperando para acceder al buffer ')
    pool.producir()
    logging.debug("Terminé de producir")
    s.release()

def consumidor (s,pool):
    logging.debug('Esperando para acceder a buffer ')
    s.acquire()
    pool.consumir()
    logging.debug("Terminé de consumir")

pool = ActivePool()
s = threading.Semaphore(0)
for i in range(4):
    c = threading.Thread(target=consumidor, name="c"+str(i), args=(s, pool))
    c.start()
for i in range(2):
    p = threading.Thread(target=productor, name="p"+str(i), args=(s, pool))
    p.start()


