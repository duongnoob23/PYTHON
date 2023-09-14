from math import *

s=input()
a=list( int(i) for i in s)
dem=0
res=""
for i in range(len(a)-1,-1,-1):
    res+=str(a[i])
    dem+=1
    if(dem==3 and i!=0):
        res+=','
        dem=0
res1=res[::-1]

print(res1)


