from PIL import Image
from zlib import *
from pwn import *
import time
p=remote('111.230.149.72',10003)
x1=p.recv(1024)
time.sleep(0.5)
p.sendline('2')
print(x1)




# data=open('C:\\Users\\assu\\Desktop\\flag.png','rb').read()
# print(data)
# data=decompressobj(data)
#
# image=Image.new('1',(25,25))
# d=image.load()
# for n,i in enumerate(data):
#     d[(n%25,n/25)]=int (i)*255
# f=open('flag.png','wb')
#
# image.save(f)