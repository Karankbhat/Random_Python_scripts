# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:42:09 2022

@author: Karan

Socket Server Multithreading
Client Side
"""

import socket

ClientSocket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_1 = '192.168.1.102'
port_1 = 12345

ClientSocket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_2 = '192.168.1.103'
port_2 = 1233

print('Waiting for connection')
try:
    ClientSocket_1.connect((host_1, port_1))
    ClientSocket_2.connect((host_2, port_2))
except socket.error as e:
    print(str(e))

Response_1 = ClientSocket_1.recv(1024)
Response_2 = ClientSocket_2.recv(1024)

print(Response_1.decode('utf-8'))
print(Response_2.decode('utf-8'))

while True:
    Input_1 = input('Say Something to Server 1: ')
    Input_2 = input('Say Something to Server 2: ')
    
    ClientSocket_1.send(str.encode(Input_1))
    ClientSocket_2.send(str.encode(Input_2))    
    
    Response_1 = ClientSocket_1.recv(1024)
    Response_2 = ClientSocket_2.recv(1024)
    
    print(Response_1.decode('utf-8'))
    print(Response_2.decode('utf-8'))    

ClientSocket_1.close()
ClientSocket_2.close()

            
            
    