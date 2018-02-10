import socket
import random
print()
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('111.230.149.72', 10003))
import time
sock1=sock.recv(1024)
print(str(sock1,encoding='utf-8'))
sock1=sock.recv(1024)
print(str(sock1,encoding='utf-8'))
sock.send((bytes("{}".format(sock1)+"\n",encoding='utf-8')))
sock1=sock.recv(1024)
print(sock1)