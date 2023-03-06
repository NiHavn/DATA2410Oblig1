
import sys
from socket import *

# Making variables to use in commandline
host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

#TCP Client socket
conSock = socket(AF_INET, SOCK_STREAM)

#Establishing serverconnection with host and port
conSock.connect((host, port))

#Sending a ET request to the server
request = "GET /" + filename + " HTTP/1.1\r\nHost: " + host + "r\n\r\n"
conSock.send(request.encode())

#Recieving response from server
msg = b''
while True:
    data = conSock.recv(2048)
    if not data:
        break

    msg += data

#Printing the message
print(msg.decode())

#Closing socket
conSock.close()
#Exiting
sys.exit()