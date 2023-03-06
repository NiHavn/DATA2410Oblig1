
import sys
from socket import *

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

conSock = socket(AF_INET, SOCK_STREAM)

conSock.connect((host, port))

request = "GET /" + filename + " HTTP/1.1\r\nHost: " + host + "r\n\r\n"
conSock.send(request.encode())

msg = b''
while True:
    data = conSock.recv(2048)
    if not data:
        break

    msg += data

print(msg.decode())


conSock.close()
sys.exit()