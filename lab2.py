import socket

# Alocate new socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Make a connection
server.bind(('0.0.0.0', 8000))
server.listen(1)

print "Waiting for connections . . ."
client, address = server.accept()
print "Connected!"
print address

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
    try:
        part = outgoing.recv(1024)
    except socket.error, exception:
        if exception.errno == 11:
            part = None
    if(part):
        client.sendall(part)
        print "> " + part
