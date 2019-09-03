
#!/usr/bin/env python3

import sys,threading,socket
def aceptarConexion(socketTCP,listaConexiones):
    while True:
        client_conn, client_addr = socketTCP.accept()
        print("Conectado a", client_addr)
        listaConexiones.append(client_conn)
        thread_read = threading.Thread(target=recibirDatos, args=[client_conn,client_addr])
        thread_read.start()

def recibirDatos(conn,addr):
        with conn:
            while True:
                print("Esperando a recibir datos... ")
                data = conn.recv(1024)
                print ("Recibido,", data,"   de ", addr)
                if not data or data=="end":
                    print("Fin")
                    break
                print("Enviando respuesta a", addr)
                conn.sendall(data)

listaConexiones=[]
host, port, numConn = sys.argv[1:4]

if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<host> <port> <num_connections>")
    sys.exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    serveraddr=(host,int(port))
    TCPServerSocket.bind(serveraddr)
    TCPServerSocket.listen(int(numConn))
    print("El servidor TCP está disponible y en espera de solicitudes")
    thread_acept = threading.Thread(target = aceptarConexion,args=[TCPServerSocket,listaConexiones])
    thread_acept.start()
    print("sigue")