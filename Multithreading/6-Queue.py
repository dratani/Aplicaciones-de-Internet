import threading
import time
import queue
import logging
from logging import exception

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s')


def consume(q):
#for i in range(10):
    try:
        item = q.get()
        logging.debug("Consume el elemento %s de cola %d", item, q.qsize())
     #   time.sleep(1)  # spend 3 seconds to process or consume the tiem
        logging.debug("Termina el proceso. cola %d", q.qsize())
  #  q.task_done()
    except(queue.Queue.empty):
        logging.debug("empty")



def producer(q):
    # the main thread will put new items to the queue

 #   for i in range(5):
        name = threading.current_thread().name
        logging.debug("Inicia producción de elementos en la cola de tamaño %d", q.qsize())
        item = "Elemento-" + str(i)
        q.put(item)
        logging.debug("Producción exitosa del item %s en la cola de tamaño %d", item, q.qsize())

  #  q.join()


if __name__ == '__main__':
    q = queue.Queue(maxsize=10)

    for i in range(15):
        t = threading.Thread(name="Consumer-" + str(i), target=consume, args=(q,))
        t.start()

    for i in range(1):
        t = threading.Thread(name="Producer-" +str(i), target=producer, args=(q,))
        t.start()

  #  q.join()
