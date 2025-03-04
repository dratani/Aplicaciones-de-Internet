# UDPPingerServer.py

import random
from socket import *

# Crear un socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Asignar dirección IP y número de puerto al socket
serverSocket.bind(('localhost', 12000))
print("El servidor UDP está disponible y en espera de solicitudes")

while True:
    # Generar un número aleatorio en el rango de 0 a 10
    rand = random.randint(0, 10)

    # Recibir el paquete del cliente junto con la dirección desde donde proviene
    message, address = serverSocket.recvfrom(1024)

    # Convertir el mensaje del cliente a mayúsculas
    message = message.upper()

    # Si rand es menor que 4, consideramos que el paquete se perdió y no respondemos
    if rand < 4:
        continue

    # De lo contrario, el servidor responde
    serverSocket.sendto(message, address)
