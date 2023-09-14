from math import *

p=[1]*(10**6+1)
ngto=[0]*(10**6+1)
def sang():
    p[0]=p[1]=0
    for i in range(2,isqrt(10**6)+1):
        if p[i]==1:
            for j in range(i*i,10**6+1,i):
                p[j]=0
    k=0
    for i in range(2,10**6):
        if p[i]==1:
            ngto[k]=i
            k+=1


sang()
a,b=map(int,input().split())
print(b,end=' ')
for i in range(0,a):
    b+=ngto[i]
    print(b,end=' ')