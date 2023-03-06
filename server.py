#import socket module
import threading
from socket import *
import sys # In order to terminate the program



def handleRequest(conSocket):
    try:
        message = conSocket.recv(2048).decode() #
        print(message) 
        filename = message.split()[1][1:]
        print(filename)
        
        f = open(filename)
        outputdata = f.read()
        
        """
        with open(filename, 'rb') as sp:
            outputdata = sp.read()
        """
        #Send one HTTP header line into socket
        conSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        conSocket.send('Content-Type: text/html\r\n'.encode())
        conSocket.send(('Content-Length: %d\r\n' % len(outputdata)).encode())
        conSocket.send('\r\n'.encode())
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata), 2048):
            conSocket.send((outputdata[i:1+2048]).encode())
    except IOError:
    #Send response message for file not found
        conSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        conSocket.send('Content-Type: text/html\r\n'.encode())
        conSocket.send('\r\n'.encode())
        conSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
    #Close client socket
    finally:
        conSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM) 
host = '127.0.0.1' #Establishes a ip for the host
port = 6789        #Defines what port communication with server happens
serverSocket.bind(('', port))
serverSocket.listen(5)


while True:
#Establish the connection print('Ready to serve...') connectionSocket, addr =
    print('Ready to serve....')
    conSocket, addr = serverSocket.accept()

    t = threading.Thread(target=handleRequest, args=(conSocket,))
    t.start()