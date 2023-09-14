from math import *

def nto(n):
    if(n<2): return False
    for i in range(2,isqrt(n)+1,1):
        if(n%i==0): return False
    return True

t=int(input())
for _ in range(t):
    s=input()
    a=list(int(i) for i in s)
    tich=1
    for i in a:
        if(i!=0):
            tich*=i
    print(tich)