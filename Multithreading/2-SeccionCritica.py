import random
import threading
import logging
import time

caracter = ""
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
def worker():
    global caracter
    logging.debug("Entré en la sección crítica")
    caracter = threading.current_thread().name
    time.sleep(random.randint(1,5))
    logging.debug("valor de caracter - %s",caracter)


h1 = threading.Thread(target=worker, name="Hilo 1")
h2 = threading.Thread(target=worker, name="Hilo 2")
h1.start()
h2.start()
h1.join()
h2.join()
