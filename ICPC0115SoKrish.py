from math import *

def giaithua(n):
    tong=1;
    for i in range(2,n+1):
        tong*=i
    return tong


def solve(n):
    m=n
    tong=0
    while(n>0):

        tong+=giaithua(n%10)
        n//=10
    if(tong==m): return True
    else: return False





t=int(input())
for _ in range(t):
    n=int(input())
    if(solve(n)): print('Yes')
    else: print('No')