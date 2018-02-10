import numpy as np
mat=[]
a=np.matrix([[5,9],[20,9]])
a=a/-57*513%26
item={
    "a":0,"b":1,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26
}
x="p h n f e t z h z z w z".split(" ")
for i,j in enumerate(item.keys()):
    item[j]=i
for j,i in enumerate(x):
    if i in item.keys():
        x=item[i]
    if j%2!=0:
        q=np.matrix([[int(i1)],[int(x)]])
        mat.append(q)
    i1=item[i]

I=a
print(I)
new_dict = {v:k for k,v in item.items()}
for i in range(0,len(mat)):
    X=a*mat[i]%26
    X=np.array(X)
    for j in range(2):
        for k in range(1):
            # print(X[j][k])
            if X[j][k] in new_dict.keys():
                print(new_dict[X[j][k]],end="")
