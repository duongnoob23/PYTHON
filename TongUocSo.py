from math import *
p= [1]*(2*(10**6+1))

def sieve():
    p[0],p[1]=0,0
    for i in range(2,isqrt(2*(10**6+1))+1):
        if p[i]==1:
            for j in range(i*i,2*(10**6+1),i):
                p[j]=i
    for i in range(2,2*(10**6+1)):
        if p[i]==1:
            p[i]=i
sieve()

t=int(input())
tong=0
for _ in range(t):
    n=int(input())
    while(n!=1):
        tong+=p[n]
        n//=p[n]
print(tong)