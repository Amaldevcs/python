from socket import *
fd = socket(AF_INET,SOCK_DGRAM)
fd.sendto('amal',('127.0.0.1',8000))
    
