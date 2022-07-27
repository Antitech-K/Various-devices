#!usr/bin/python
#-*-coding:utf-8-*-

import time
import os
import subprocess


video_int = "ffplay /dev/video-int"
video_out = 'ffplay /dev/video-out'

x = 0
while x != 1000: 
    try:
        subprocess.check_output(video_int, shell = True, timeout = 5)
    except subprocess.TimeoutExpired:
        pass
    time.sleep (2)
    try:
        subprocess.check_output(video_out, shell = True, timeout = 5)
    except subprocess.TimeoutExpired:
        pass
    time.sleep(2)


#os.system("timeout 5s  [ffplay /dev/video-int]")
#time.sleep(3)

