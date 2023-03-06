#import socket module
import threading
from socket import *
import sys # In order to terminate the program



def handleRequest(conSocket):
    try:
        #Recieving the request from the client
        message = conSocket.recv(2048).decode() 
        filename = message.split()[1][1:] #the[1][1:] specifies what portion of the file name to send
        f = open(filename)
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        conSocket.send('HTTP/1.1 200 OK\r\n'.encode()) #Statusline
        conSocket.send('Content-Type: text/html\r\n'.encode())
        conSocket.send(('Content-Length: %d\r\n' % len(outputdata)).encode())
        conSocket.send('\r\n'.encode())     #Makes the end of the response

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata), 2048):
            conSocket.send((outputdata[i:1+2048]).encode())
        #the for-loop goes sends the characters from 0 to the length of outdata
    except IOError:  #Used for exceptionhandling, if the server ant find the specified file, it will return an 404 exception
    #Send response message for file not found
        conSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())  #404 response if server cant find file
        conSocket.send('Content-Type: text/html\r\n'.encode())
        conSocket.send('\r\n'.encode())
        conSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
    #Close client socket
    finally:
        conSocket.close() #Makes sure the program exits when done

serverSocket = socket(AF_INET, SOCK_STREAM) #Server socket
host = '127.0.0.1' #Establishes a host-ip for the host
port = 6789        #Defines what port communication with server happens
serverSocket.bind(('', port))  #
serverSocket.listen(5) #Max nuber of users at the same time


while True:
#Establish the connection print('Ready to serve...') connectionSocket, addr =
    print('Ready to serve....')
    conSocket, addr = serverSocket.accept()
    t = threading.Thread(target=handleRequest, args=(conSocket,))
    t.start()