#!/usr/bin/env python3

import socket
import time
HOST = "127.0.0.1"  # El hostname o la IP del servidor
PORT = 12345  # El puerto que usa el servidor
buffer_size = 1024
archivo = open("../../libros/MobyDick.txt", "r")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    for linea in archivo.readlines():
        print("Enviando mensaje",linea)
        TCPClientSocket.sendall(str.encode(linea))
        print("Esperando una respuesta...")
        data = TCPClientSocket.recv(buffer_size)
        print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())
       # time.sleep(1)
    archivo.close()
