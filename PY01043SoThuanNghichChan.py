from math import *
def tn(a):
    dem=0
    while(a>0):
        if(a%10%2!=0): return 0
        dem+=1
        a//=10
    if(dem%2==0):return 1
    else: return 0

t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(22,n,2):
        n=int( str(i)[::-1] )
        if(i==n and tn(i)==1):
            print(i,end=' ')
    print()
