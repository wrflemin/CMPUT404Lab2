import socket
import os
# Alocate new socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Make a connection
server.bind(('0.0.0.0', 8000))
server.listen(1)
while True:
    print "Waiting for connections . . ."
    client, address = server.accept()
    print "Connected!"
    print address
    pid = os.fork()
    if (pid == 0): #we are in the child process
        outgoing = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        outgoing.connect(("www.google.ca", 80))
        outgoing.setblocking(0)
        client.setblocking(0)

        while True:
            try:
                part = client.recv(1024)
            except socket.error, exception:
                if exception.errno == 11:
                    part = None
                else:
                    raise
            if (part):
                outgoing.sendall(part)
                print "< " + part
            if (part is not None and len(part) == 0):
                exit(0)
            try:
                part = outgoing.recv(1024)
            except socket.error, exception:
                if exception.errno == 11:
                    part = None
            if (part is not None and len(part) == 0):
                exit(0)
            if(part):
                client.sendall(part)
                print "> " + part
