from math import *

def solve(s):
    tong=0
    tich=0
    for i in range(len(s)):
        if(i%2==0):
            tong+=int(s[i])
        else:
            if(int(s[i])!=0):
                if(tich==0):
                    tich=int(s[i])
                else:
                    tich*=int(s[i])
    print(tong,end=' ')
    print(tich)




t=int(input())
for _ in range(t):
    s=input()
    solve(s)