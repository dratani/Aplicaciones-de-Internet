
import queue
import threading

# este thread se bloquea esperando que venga algo en la cola,
# lo unico que hace es imprimirlo. Si el mensaje es quit finaliza
class Reader(threading.Thread):
   def __init__(self, in_queue):
       threading.Thread.__init__(self)
       self.in_queue = in_queue

   def run(self):
       while True:
           msg = self.in_queue.get()
           if msg == 'quit':
               print ('reader se va!')
               break

           print ('leido ' + msg)

# este thread se bloquea esperando que venga algo en la cola de entrada,
# cuando llega algo lo escribe al reves en la cola de salida.
class Writer(threading.Thread):
   def __init__(self, in_queue, out_queue):
       threading.Thread.__init__(self)
       self.in_queue = in_queue
       self.out_queue = out_queue

   def run(self):
       while True:
           msg = self.in_queue.get()
           if msg == 'quit':
               print ('writer se va!')
               self.out_queue.put(msg)
               break

           print ('escrito ' + msg)

           self.out_queue.put(msg[::-1])

# aca creo un lector y un escritor, le doy de salida a writer la
# entrada de reader, por lo tanto lo que escriba writer lo va a
# leer reader al reves el recorrido es asi:
# mensaje -> entra a writer -> lo invierte -> lo envia a la salida -> entra a reader
def test():
   in_queue =  queue.Queue()
   out_queue =  queue.Queue()
   reader = Reader(out_queue)
   writer = Writer(in_queue, out_queue)

   reader.start()
   writer.start()

   in_queue.put('buenas')
   in_queue.put('como va')
   in_queue.put('quit')

if __name__ == '__main__':
   test()

