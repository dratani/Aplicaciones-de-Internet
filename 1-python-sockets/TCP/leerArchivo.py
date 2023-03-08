#Ejemplo lectura archivo
import time
archivo = open("../../libros/Bibla.txt", "r")
for linea in archivo.readlines():
    print(linea)
    time.sleep(0.1)
archivo.close()