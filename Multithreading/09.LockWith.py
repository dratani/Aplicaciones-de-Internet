import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker_with(lock):
    with lock:
        logging.debug('Bloqueo adquirido vía with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Bloqueo adquirido de manera directa')
    finally:
        lock.release()


lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()