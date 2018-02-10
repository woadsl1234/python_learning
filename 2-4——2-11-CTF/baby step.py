from pyDes import *
data="635353528311"
k=des("DESCRYPT",CBC,"10000309",pad=None,padmode=PAD_PKCS5)
d=k.encrypt(data)
print("%s" %d)