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
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Ejecutando append: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Ejecutando remove: %s', self.active)


def worker(s, pool):
    logging.debug('Esperando para acceder al grupo ')
    with s:
        logging.debug("Adquirí el semáforo")
        name = threading.current_thread().name
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)
        logging.debug("Haciendo el release del semáforo")


pool = ActivePool()
s = threading.Semaphore(3)
for i in range(4):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()
