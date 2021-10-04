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


def consumer(mutex,semaforo):
    global buffer

    """wait for the condition and use the resource"""
    logging.debug('Iniciando hilo consumidor')
    # t = threading.currentThread()
    while 1:
        logging.debug('Esperando recurso')
        semaforo.acquire()
        with mutex:
            logging.debug("Productos=%s",buffer)

            buffer.remove("producto")
            logging.debug("removí un recurso")
        time.sleep(1)


def producer(mutex, CondMaxBuffer,semaforo):
    global buffer
    """set up the resource to be used by the consumer"""
    logging.debug('Iniciando el hilo productor')
    while 1:
        with CondMaxBuffer:
            if len(buffer) < 3:
                CondMaxBuffer.notify()
                logging.debug("pueden seguir produciendo")
                with mutex:
                    logging.debug("produciendo")
                    buffer.append("producto")
                    logging.debug("Productos:%s",buffer)
                logging.debug('Poniendo los recursos disponibles')
                semaforo.release()
            else:
                logging.debug("deteniendo producción")
                CondMaxBuffer.wait()
        time.sleep(1)


mutex = threading.Lock()
semaforo = threading.Semaphore(0)
condicion_Max_buffer = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(mutex,semaforo))
c2 = threading.Thread(name='c2', target=consumer, args=(mutex,semaforo))
p = threading.Thread(name='p', target=producer, args=(mutex, condicion_Max_buffer,semaforo))
p2 = threading.Thread(name='p2', target=producer, args=(mutex, condicion_Max_buffer,semaforo))
c1.start()
#time.sleep(2)
#c2.start()
#time.sleep(2)
p.start()
p2.start()
