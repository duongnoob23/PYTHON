import math
from math import *

prime = [True] *(10 ** 6 +1)
def sang():
    prime[0]=prime[1]=False
    for i in range(2, isqrt(10**6)):
        if prime[i]:
            for j in range(i*i,10 ** 6,i):
                prime[j]=False

def sodao(a):
    tmp=0
    while(a>0):
        tmp=tmp*10+a%10
        a//=10
    return tmp

sang()


t=int(input())
for _ in range(t):
    n=int(input())
    m=sodao(n)

    if(gcd(n,m)==1):
        print('YES')
    else:
        print('NO')
