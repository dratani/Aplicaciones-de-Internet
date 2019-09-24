import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def lock_holder(lock):
    logging.debug('Iniciando')
    while True:
        lock.acquire()
        try:
            logging.debug('Adquirido')
            time.sleep(0.5)
        finally:
            logging.debug('liberado')
            lock.release()
        time.sleep(0.5)
    return

def worker(lock):
    logging.debug('Iniciando')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Intentando adquirir')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteración %d: Adquirido', num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteración %d: No adquirido', num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Realizado después de  %d iteraciones', num_tries)


lock = threading.Lock()

holder = threading.Thread(target=lock_holder, args=(lock,), name='poseedorCandado')
holder.setDaemon(True)
holder.start()

worker = threading.Thread(target=worker, args=(lock,), name='trabajador')
worker.start()