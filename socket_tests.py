# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:42:09 2022

@author: Karan

Socket Server Multithreading
"""

## Import Libraries
import socket
import os
import sys
from _thread import *

## Declare Socket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'rpi4.local'

try:
    remote_ip = socket.gethostbyname( host )
    
except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
    
print ('Ip address of ' + host + ' is ' + remote_ip)    

# host = '127.0.0.1'
# port = 1233
# ThreadCount = 0

# ## Bind host, port
# try:
#     ServerSocket.bind((host, port))
    
# except socket.error as e:
#     print (str(e))
    
# print('Waiting for a Connection..')
# ServerSocket.listen(5)

# def threaded_client (connection):
#     connection.send(str.encode('Welcome to the Server'))
    
#     while True:
#         data = connection.recv(2048)
#         reply = 'Server Says: ' + data.decode('utf-8')
        
#         if not data:
#             break
        
#         connection.sendall(str.encode(reply))
        
#     connection.close()
    
# while True:
#     Client, address = ServerSocket.accept()
#     print('Connected to: ' + address[0] + ':' + str(address[1]))
#     start_new_thread(threaded_client, (Client, ))
#     ThreadCount += 1
    
#     print('Thread Number: ' + str(ThreadCount))
    
# ServerSocket.close()

            
            
    