from math import *

f=[0]*94

def fibonaci():
    f[0]=0
    f[1]=1
    for i in range(2,93):
        f[i]=f[i-1]+f[i-2]

fibonaci()
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        print(f[i],end=' ')
    print()