import random
ra=random.randint(1,50)
for i in range(1,4):
    x=input()
    if x==ra:
        print("猜对了")
    else:
        print("猜错了，这是第{}次，总共三次机会".format(i))
