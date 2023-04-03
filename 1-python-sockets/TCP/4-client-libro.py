#!/usr/bin python3

import socket
import time
HOST = "127.0.0.1"  # Hostname o  dirección IP del servidor
PORT = 65432  # Puerto del servidor
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    print("Enviando mensaje...")
    with open("../../libros/MobyDick.txt", "r") as archivo:
        for linea in archivo.readlines():
            print(linea)
            TCPClientSocket.sendall( str.encode(linea))
    print("Terminé")
