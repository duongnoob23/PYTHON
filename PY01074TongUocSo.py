from math import *

p = [1]*(10**6+1)
def sangsongto():
    p[0]=p[1]=0
    for i in range(2,isqrt(10**6+1)):
        if(p[i]):
            for j in range(i*i,10**6+1):
                p[j]=1

t=int(input())
sangsongto()
print(p[2])
