import random
import threading
import logging
import time

caracter = ""
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def worker(lock):
    global caracter
    lock.acquire()
    try:
        logging.debug("Entré en la sección crítica")
        caracter = threading.current_thread().name
        time.sleep(random.randint(1, 5))
        logging.debug("valor de caracter=" + caracter)
    finally:
        lock.release()


lock = threading.Lock()
h1 = threading.Thread(target=worker, name="Hilo 1", args=(lock,))
h2 = threading.Thread(target=worker, name="Hilo 2", args=(lock,))
h1.start()
h2.start()
h1.join()
h2.join()
