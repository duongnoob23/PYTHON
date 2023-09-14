from math import *

def ngto(n):
    for i in range(2,isqrt(n)+1):
        if(n%i==0): return False
    return n>1


t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(13,n+1,2):
        s=str(i)
        if( s!=s[::-1] and ngto(i) and ngto(int(s[::-1])) and int(s[::-1])<n): print(i,end=' ')
    print()

