from math import *

def ngto(n):
    for i in range(2,isqrt(n)+1):
        if(n%i==0): return False
    return n>1

def solve(n):
    tong=0

    while(n>0):
        if(not ngto(n%10)): return False
        tong+=n%10
        n//=10
    if(ngto(tong)): return True
    else: return False
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(n)
    if(ngto(n) and ngto(int(s[::-1])) and solve(n)): print('Yes')
    else: print('No')
