from math import *

def ngto(n):
    for i in range(2,isqrt(n)+1):
        if(n%i==0): return 0
    return n>1

def solve(n):
    dau=int(n[:3])
    cuoi=int(n[-3:])
    if(ngto(dau)+ngto(cuoi)==2):
        print('YES')
    else:
        print('NO')

t=int(input())
for _ in range(t):
    s=input()
    solve(s)