#holi  aaaa
import socket
HOST = "127.0.0.1"  # El hostname o IP del servidor
PORT = 54321  # El puerto que usa el servidor
bufferSize = 1024
msgFromServer = "Hola cliente UDP"
bytesToSend = str.encode(msgFromServer)

with  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind((HOST, PORT))

    print("Servidor UDP activo, esperando peticiones")
    # Listen for incoming datagrams
    msgFromServer = "Hola cliente UDP"

    bytesToSend = str.encode(msgFromServer)
    while (True):
        data,address = UDPServerSocket.recvfrom(bufferSize)

        print("Mensaje del cliente:{}".format(data))
        print("Ip del cliente:{}".format(address))

        # Enviando una respuesta al cliente
        UDPServerSocket.sendto(bytesToSend, address)