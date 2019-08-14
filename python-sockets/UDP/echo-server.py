import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 54321  # The port used by the server
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

with  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind((HOST, PORT))

    print("UDP server up and listening")
    # Listen for incoming datagrams
    msgFromServer = "Hello UDP Client"

    bytesToSend = str.encode(msgFromServer)
    while (True):
        data,address = UDPServerSocket.recvfrom(bufferSize)

        print("Message from Client:{}".format(data))
        print("Client IP Address:{}".format(address))

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)