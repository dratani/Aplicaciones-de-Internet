import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('Esperando por evento inicio')
    event_is_set = e.wait()
    logging.debug('evento : %s', event_is_set)


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        logging.debug('Esperando evento inicio a destiempo')
        event_is_set = e.wait(t)
        logging.debug('evento: %s', event_is_set)
        if event_is_set:
            logging.debug('Procesando evento')
        else:
            logging.debug('haciendo otro trabajo')


e = threading.Event()
t1 = threading.Thread(name='Bloqueante',
                      target=wait_for_event,
                      args=(e,))
t1.start()

t2 = threading.Thread(name='No Bloqueante',
                      target=wait_for_event_timeout,
                      args=(e, 2))
t2.start()

logging.debug('Esperando antes de llamar a Event.set()')
time.sleep(3)
e.set()
logging.debug('El evento está iniciado')