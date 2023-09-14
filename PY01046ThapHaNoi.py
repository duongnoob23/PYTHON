from math import *

def chuyen(n,a,b,c):
    if(n==1):
        print(a+ " -> "+c)
    else:
        chuyen(n-1,a,c,b)
        chuyen(1,a,b,c)
        chuyen(n-1,b,a,c)



n=int(input())
chuyen(n,'A','B','C')