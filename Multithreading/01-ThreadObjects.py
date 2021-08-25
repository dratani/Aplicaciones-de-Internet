import threading

def worker(num):
    """hilo función trabajador"""
    print ('Trabajador',num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()