#--------------------------------------------------
#Restricciones
# 1) En un taller de costura se elaboran chamarras.
# Una persona está continuamente fabricando mangas
# que va depositando a un cesto.
# El cesto tiene una capacidad limitada, cuando se
# llena, la costurera deja de coser hasta que haya
# un espacio disponible.
# Otra persona está continuamente fabricando los
# cuerpos, cuenta con otra canasta con capacidad
# limitada, cuando se llena detiene el proceso de
# elaboración. La tercer persona se encarga de
# ensamblar la prenda, toma dos mangas de la cesta
# de mangas y un cuerpo de la cesta correspondiente
# y las une para formar una prenda.
#
# Implementar un código que sincronice a las tres
# personas de forma que las dos primeras no avancen
# si su cesta está llena y que la tercer persona no
# avance si le faltan piezas para hacer la nueva
# prenda
#--------------------------------------------------

import threading
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-2s) %(message)s')

class Taller(object):
    def __init__(self, start=0):
        self.condicionMangas = threading.Condition()
        self.conicionCuerpos = threading.Condition()
        self.mangas=0
        self.cuerpos=0
    def incrementarManga(self):
        self.condicionMangas.acquire()
        try:
            if self.mangas>=10:
                logging.debug("No hay espacio para mangas")
                self.condicionMangas.wait()
            else:
                self.mangas+=1
        finally:
            self.condicionMangas.release()

    def getMangas(self):
        return (self.mangas)
    def crearCuerpo(self):
        self.cuerpos+=1

    def decrementarManga(self):
        with self.condicionMangas:
            self.mangas-=1
            self.condicionMangas.notify_all()

def crearManga(Taller):
    while(Taller.getMangas()<=10):
        logging.debug('crear, manga=%s',Taller.getMangas())
        Taller.incrementarManga()
        time.sleep(1)
def tomarMangas(Taller):
    while(taller.getMangas()>0):
        logging.debug("tomar, mangas=%s",taller.getMangas())
        Taller.decrementarManga()
        time.sleep(9)
def crearCuerpos(Taller):
    logging.debug('Creando cuerpos')

taller = Taller()
mangas = threading.Thread(name='personaMangas', target=crearManga,args=(taller,) )
tomarM = threading.Thread(name='tomarMangas', target=tomarMangas,args=(taller,) )
#cuerpos = threading.Thread(name='personaCuerpos', target=crearCuerpos(taller))

mangas.start()
tomarM.start()
tomarM.join()
mangas.join()