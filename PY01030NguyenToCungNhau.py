from math import *


n,k=map(int,input().split())
l=(10**(k-1))
r=10**k
dem=0
for i in range(l,r):
    if(gcd(n,i)==1):
        dem+=1
        print(i,end=' ')
        if(dem==10):
            print()
            dem=0






