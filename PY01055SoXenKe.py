from math import *

def solve(s):
    if(len(s)%2==0 or s[0]==s[1]): return 0
    for i in range(2,len(s),2):
        if(s[i]!=s[0]): return 0
    return 1




t=int(input())
for _ in range(t):
    s=input()
    if(solve(s)==1): print('YES')
    else: print('NO')