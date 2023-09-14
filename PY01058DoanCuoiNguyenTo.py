from math import *


def ngto(n):

    for i in range(2,isqrt(n)+1):
        if(n%i==0): return 0
    return n>1

def solve(s):
    st=s[-4:]
    if(ngto(int(st))): print('YES')
    else:print('NO')


t=int(input())
for _ in range(t):
    s=input()
    solve(s)

