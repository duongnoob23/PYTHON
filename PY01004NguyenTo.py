import math
def nto(a):
    if(a<2): return 0
    for i in range(2,math.isqrt(a)+1):
        if(a%i==0): return 0
    return 1

def ucln(a,b):
    while( a*b!=0):
        if(a>b): a%=b
        else: b%=a

    return a+b

t=int(input())
for _ in range(t):
    n=int(input())
    dem=0
    for x in range(0,n):
        if(ucln(x,n)==1):
            dem+=1
    if(nto(dem)): print('YES')
    else: print('NO')

