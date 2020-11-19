import socket
newSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSoc.connect(('soft.anztradebdltd.com', 80))
cmd = 'GET http://soft.anztradebdltd.com HTTP/1.0\n\n'.encode()
newSoc.send(cmd)

while True:
    data = newSoc.recv(512)

    if(len(data)<1):
        break;
    print(data.decode())

newSoc.close()
