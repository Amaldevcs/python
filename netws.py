from socket import *
fd = socket(AF_INET,SOCK_DGRAM)
fd.bind(('127.0.0.1',8000))
print  fd.recvfrom(1)



