from math import *

def max1(s,a,b):
    s3=""
    for i in range(len(s)):
        if(s[i]=='a'): s3[i]='b'
        else:s3[i]=s[i]
    return s3

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    s=input()
    s1=input()
    max1(s,a,b)



