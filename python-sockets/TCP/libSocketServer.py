import socket, threading


def aceptarConexion(socketTCP,listaConexiones):
    while True:
        client_conn, client_addr = socketTCP.accept()
        print("Conectado a ", client_addr)
        listaConexiones.append(client_conn)
        thread_read = threading.Thread(target=recibirDatos, args=[client_conn,client_addr])
        thread_read.start()

def recibirDatos(conn,addr):
        with conn:
            while True:
                print("Esperando a recibir datos... ")
                data = conn.recv(1024)
                print ("Recibido,", data,"   de ", addr)
                if not data:
                    break
                print("Enviando respuesta a", addr)
                conn.sendall(data)