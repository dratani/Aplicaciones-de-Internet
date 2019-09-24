import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Esperando para bloquear')
        self.lock.acquire()
        try:
            logging.debug('Bloqueo adquirido')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Durmiendo %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Hecho')


counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    t.join()

logging.debug('Contador: %d', counter.value)