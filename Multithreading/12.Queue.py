import threading
import time
import queue
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s')
def consume(q):
    while (True):

        item = q.get();
        logging.debug("Consume el elemento %s de cola %d",item, q.qsize())
        time.sleep(3)  # spend 3 seconds to process or consume the tiem
        logging.debug("Termina el proceso. cola %d",q.qsize())
        q.task_done()


def producer(q):
    # the main thread will put new items to the queue

    for i in range(10):
        name = threading.currentThread().getName()
        logging.debug("Inicia producción de elementos en la cola de tamaño %d",q.qsize())
        item = "Elemento-" + str(i)
        q.put(item)
        logging.debug("Producción exitosa del item %s en la cola de tamaño %d",item,q.qsize())

    q.join()


if __name__ == '__main__':
    q = queue.Queue(maxsize=3)

    threads_num = 3  # three threads to consume
    for i in range(threads_num):
        t = threading.Thread(name="Consumer-" + str(i), target=consume, args=(q,))
        t.start()

    # 1 thread to procuce
    t = threading.Thread(name="Producer", target=producer, args=(q,))
    t.start()

    q.join()
