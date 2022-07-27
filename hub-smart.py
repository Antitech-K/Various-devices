#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyACM1'
ser.timeout = 2
ser.rtscts = False
ser.open()
print (ser)

'''
for i in "*SYS0?":
    ser.write(i.encode("utf-8"))
print (ser.readline())    
time.sleep(2)'''

for j in range(6):
    #time.sleep(1)
    command_name = ''
    command = "*PWRSW0" + str(j) + "0?"
    for k in command:
        command_name += k
        ser.write(k.encode("utf-8"))
    time.sleep(1)
    ser.write('/n'.encode("utf-8"))
    print ('отправлено ->', command_name, "получено ->", ser.readline())  
    ser.flushInput()
     
command_name = ''
for i in "*PORTSTAT?":
    command_name += i
    ser.write(i.encode("utf-8"))
print ("отправлено ->", command_name, "получено ->", ser.readline())

ser.close()
#print ("Открыт ли порт-", ser.is_open)
