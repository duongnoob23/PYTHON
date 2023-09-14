from math import *


def ngto(n):

    for i in range(2,isqrt(n)+1):
        if(n%i==0): return 0
    return n>1

def solve(s):
    for i in range(len(s)):
        if( ngto(i)-ngto(int(s[i]))!=0):
            return False
    return True

t=int(input())
for _ in range(t):
    s=input()
    if(solve(s)): print('YES')
    else: print('NO')

