from math import floor
import random 
import numpy as np
n=4
m=5
mat=np.zeros((m, n))

for i in range(0,m):
    for j in range(0,n):
        mat[i][j]=floor(random.random()*10)        
print(mat)

for j in range(0,n):
    if  j%2==0:
        for i in range(0,m):
            print("le",mat[i,j], sep=' ' ,end=' ')
    else:
        x=range(0, m).__reversed__()
        for i in x:
            print("fel", mat[i,j] ,sep=' ', end=' ')