#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket
#Write your code here
host = '127.0.0.1'
port = 6789
serverSocket.bind((host, port))
serverSocket.listen(1)
#End of your code
while True:
#Establish the connection print('Ready to serve...') connectionSocket, addr =
    print('Ready to serve....')
    conSocket, addr = serverSocket.accept()
    try:
        message = conSocket.recv(2048).decode()
        print(message) 
        filename = "." + message.split()[1]
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
        conSocket.close()
    except IOError as e:
    #Send response message for file not found
        conSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        conSocket.send('Content-Type: text/html\r\n'.encode())
        conSocket.send('\r\n'.encode())
        conSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
        print(e)
        conSocket.close()
    #Close client socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data