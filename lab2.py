import socket

# Alocate new socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make a connection
server.bind(('0.0.0.0', 8000))
server.listen(1)

print "Waiting for connections . . ."
client, address = server.accept()
print "Connected!"
print address
