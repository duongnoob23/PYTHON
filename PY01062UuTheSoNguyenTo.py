from math import *

def ngto(n):
    for i in range(2,isqrt(n)+1):
        if(n%i==0):
            return False
    return True

def solve(s):
    dem=0
    for i in range(len(s)):
        if(ngto(int(s[i]))):
            dem+=1

    if(ngto(len(s)) and dem>len(s)-dem): print('YES')
    else: print('NO')



t=int(input())
for _ in range(t):
    s=input()
    solve(s)
