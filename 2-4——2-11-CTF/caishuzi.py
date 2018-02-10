import numpy
import socket
import random
import time

while(True):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect(('111.230.149.72', 10002))
    except:
        time.sleep(10)
    i=0
    with open("cai1.txt",'a') as cai:
        while(True):
            try:
                sock1=sock.recv(1024)
            except:
                break
            if b''==sock1:
                break
            if b'hgame{' in sock1:
                flag=open('flag2.txt','w+')
                flag.write(str(sock1,encoding='utf-8'))
                flag.close()
            x1=str(sock1,encoding='utf-8')
            print(x1)
            if i==2:
                cai.write(x1[45:60])
            x="1715628272"
            sock.send((bytes("{}\n".format(x),encoding='utf-8')))
            i+=1
            print(i)

