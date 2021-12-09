import socket
import cv2 as cv



sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)
# sender.sendto(str.encode('hello'),('192.168.16.11',7778))

perLength = int((480*640*3)/20)
realLength = perLength + 1


cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, (480,640))
    decimal = frame.flatten()
    str = decimal.tobytes()
    #480*640*3/20
    for i in range(20):
        sender.sendto(bytes([i]) + str[i*perLength:(i+1)*perLength], ('192.168.16.11',7778))
         
    pass
cv.destoryAllWindows()