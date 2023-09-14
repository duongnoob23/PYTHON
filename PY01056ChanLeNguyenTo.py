from math import *

def ngto(s):
    if(s<2): return 0
    for i in range(2,isqrt(s)+1):
        if(s%i==0): return 0
    return 1


def solve(s):
    for i in range(0,len(s),2):
        if(int(s[i])%2!=0): return False
    for i in range(1,len(s),2):
        if(int(s[i])%2==0): return False
    tong=sum(int(i) for i in s)
    if(ngto(tong)==0): return False
    return True




t=int(input())
for _ in range(t):
    s=input()
    if(solve(s)): print('YES')
    else: print('NO')