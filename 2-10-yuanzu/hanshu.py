def nested_sum(x):
    t=0
    for i in x:
        if type(i)==list:
            for j in i:
                t+=j
        else:
            t+=i
    print(t)
    return t
def cumsum(t):
    x=0
    l=[]
    for i in t:
        x+=i
        l.append(x)
    print(l)
    return l
def middle(t):
    l=t[1:-1]
    print(l)
    return l
def chop(t):
    del t[0]
    del t[-1]
    return t
l=[[1,2],[3],[4,5,6]]
nested_sum(l)
t=[1,2,3,4]
cumsum(t)
middle(t)
chop(t)
print(t)
