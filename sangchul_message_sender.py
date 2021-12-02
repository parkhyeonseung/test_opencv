import socket

sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)

sender.sendto('Hello Sender',('192.168.16.11',7778))

