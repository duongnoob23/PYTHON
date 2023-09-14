from math import *


t=int(input())
for _ in range(t):
    s=input()
    s+='!'
    i=0
    dem=1
    while(i<len(s)-1):
        if(s[i]==s[i+1]):
            dem+=1
            i+=1
        else:
            print(dem,end='')
            print(s[i],end='')
            dem=1
            i+=1
    print()