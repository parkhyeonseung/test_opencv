import socket

receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
receiver.bind(('192.168.16.12',7778))

while True:

    bytepair = receiver.recvfrom(1024)

    message = bytepair[0]
    address = bytepair[0]

    print('message : ', message)
    print('Address : ', address)



