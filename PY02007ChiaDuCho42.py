from math import *

t=int(input())
for j in range(t):
    n=int(input())
    res=0
    for i in range(2,isqrt(n)+1):

        while(n%i==0):
            res=i
            n//=i
    if(n!=1): res=n
    if(res>5): print()


