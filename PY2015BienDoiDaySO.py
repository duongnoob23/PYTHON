from math import *

def check(a,b,c,d):
    if(a==b and b==c and c==d): return True
    else: return False

while(True):

    dem=0
    a=list(map(int ,input().split()))
    dem=-1
    if(a.count(0)==4): break
    while(a.count(0)!=4):
        tmp=a.copy()
        for i in range(0,4,1):
            a[i]=abs(tmp[i]-tmp[(i+1)%4])
        dem+=1
    print(dem)
