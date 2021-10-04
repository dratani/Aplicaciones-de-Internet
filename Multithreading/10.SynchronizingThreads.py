import logging
import threading
import time

# Agregar el buffer finito (10 elementos)
# Agregar condición de parada del productor
# Agregar condición de consumo
# Agregar producción y el consumo (manipulación de buffer)
buffer = []
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )


def consumer(cond):
    global buffer

    """wait for the condition and use the resource"""
    logging.debug('Iniciando hilo consumidor')
    # t = threading.currentThread()
    while 1:
        with cond:
            logging.debug('Esperando recurso')
            cond.wait()
            print(buffer)
            buffer.remove("producto")
            logging.debug("removí un recurso")

        time.sleep(1)


def producer(cond, produccion):
    global buffer
    """set up the resource to be used by the consumer"""
    logging.debug('Iniciando el hilo productor')
    while 1:
        with produccion:
            if len(buffer) < 10:
                produccion.notify()
                logging.debug("empiecen a producir")
                with cond:
                    logging.debug("produciendo")
                    buffer.append("producto")
                    logging.debug('Poniendo los recursos disponibles')
                    cond.notifyAll()
            else:
                logging.debug("deteniendo producción")
                produccion.wait()
        time.sleep(1)


condition = threading.Condition()
conditionProductor = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition, conditionProductor))
p2 = threading.Thread(name='p2', target=producer, args=(condition, conditionProductor))
c1.start()
#time.sleep(2)
c2.start()
#time.sleep(2)
p.start()
p2.start()
