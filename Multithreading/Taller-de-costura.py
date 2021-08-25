import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-2s) %(message)s')

class Taller(object):
    def __init__(self, start=0):
        self.condicionMangasMAX = threading.Condition()
        self.condicionMangasMIN = threading.Condition()
        self.mangas = 0
        self.cuerpos = 0

    def incrementarManga(self):

        with self.condicionMangasMAX:
            if self.mangas >= 10:
                logging.debug("No hay espacio para mangas")
                self.condicionMangasMAX.wait()
            else:
                self.mangas += 1
                logging.debug("Manga creada, mangas=%s",self.mangas)

        with self.condicionMangasMIN:
            if self.mangas >= 2:
                logging.debug("Existen suficientes mangas")
                self.condicionMangasMIN.notify()

    def decrementarManga(self):
        with self.condicionMangasMIN:
            while not self.mangas>=2:
                logging.debug("Esperando mangas")
                self.condicionMangasMIN.wait()
            self.mangas -= 2
            logging.debug("Mangas tomadas, mangas=%s",self.mangas)

        with self.condicionMangasMAX:
            logging.debug("Hay espacio para mangas")
            self.condicionMangasMAX.notify()

    def getMangas(self):
        return (self.mangas)

    def crearCuerpo(self):
        self.cuerpos += 1

def crearManga(Taller):
    while (Taller.getMangas() <= 10):
        Taller.incrementarManga()
        time.sleep(5)


def tomarMangas(Taller):
    while (taller.getMangas() >= 0):
        Taller.decrementarManga()
        time.sleep(1)


def crearCuerpos(Taller):
    logging.debug('Creando cuerpos')


taller = Taller()
mangas = threading.Thread(name='personaMangas', target=crearManga, args=(taller,))
tomarM = threading.Thread(name='tomarMangas', target=tomarMangas, args=(taller,))
# cuerpos = threading.Thread(name='personaCuerpos', target=crearCuerpos(taller))

mangas.start()
tomarM.start()
tomarM.join()
mangas.join()
