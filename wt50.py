#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import serial
import time

ser = serial.Serial()
ser.baudrate = 38400
ser.port = '/dev/rfcomm0'
ser.timeout = 2
ser.rtscts = False
ser.open()
print (ser)


'''
for i in "*SYS0?":
 '''#   ser.write(i.encode("utf-8"))
print (ser.readline())    
time.sleep(2)


    #time.sleep(1)
ser.write("0x11, 0xDE, 0xF8, 0x33, 0xEA, 0x14, 0xDA, 0xD0, 0x17, 0x0E, 0x55, 0xB4, 0xAA, 0xA2, 0x77, 0x01".encode("utf-8"))
time.sleep(1)
#ser.write('/n'.encode("utf-8"))
#print ('отправлено ->', command_name, "получено ->", ser.readline())  
ser.flushInput()
     

'''
command_name = ''
for i in "*PORTSTAT?":
    command_name += i
    ser.write(i.encode("utf-8"))
print ("отправлено ->", command_name, "получено ->", ser.readline())
'''
ser.close()
#print ("Открыт ли порт-", ser.is_open)
