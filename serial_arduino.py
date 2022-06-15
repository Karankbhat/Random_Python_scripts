# -*- coding: utf-8 -*-
"""
Serial communication with Arduino

Author: Karan K. Bhat
"""

import serial
import time

def write_read(x):
    arduino = serial.Serial(port='COM5', baudrate=115200, timeout=1)
    arduino.write(bytes(x, 'utf-8'))
    arduino.flushOutput()
    bytes_cnt = 1;
    data = b''
    
    read_ack = arduino.readline()
    print(read_ack)
        
    
    if (read_ack == 'Acknowledged'):
        arduino.write(bytes('ready', 'utf-8'))
        while (len(data) < 32768):
            bytes_cnt = arduino.inWaiting()
            data = arduino.read(bytes_cnt)

    else:
        arduino.flushInput()       
        arduino.close()
        return b'0x01'

    arduino.flushInput()
    arduino.close()    
    return data

while True:
    command = input("Enter command: ")

#     value = write_read(command)
#     print(value)
