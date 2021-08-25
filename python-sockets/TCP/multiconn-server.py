#!/usr/bin/env python3
#
import sys
import socket
import selectors
import types
#
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('aceptado', conn, ' de', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('respondiendo', repr(data), 'a', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('cerrando', conn)
        sel.unregister(conn)
        conn.close()

with socket.socket() as sock:
    sock.bind(('localhost', 1234))
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        print("Esperando evento...")
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)