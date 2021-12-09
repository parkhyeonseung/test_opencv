import socket
import cv2
import numpy as np

receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
receiver.bind(('192.168.16.12',7778))

perlength = int((480*640*3)/20)
realength = perlength +1 
array = []
num_array=b''   ## 2진수
while True:

    message,address = receiver.recvfrom(realength)

    array[message[0]] = message[1:46081]
    if message[0] == 19:
        for i in range(20):
            num_array += array[i]
        frame = np.fromstring(num_array,dtype = np.uint8)
        frame = frame.reshape(480,640,3)
        cv2.waitKey(1)
        cv2.imshow('c',frame)