
import math
def check1(n):
    while(n>10):
        if(math.fabs(n%10-n//10%10)!=2):
            return False
        n//=10
    return True

def tong(n):
    tong=0
    while(n>0):
        tong+=n%10
        n//=10

    return tong

t=int(input())
for _ in range(t):
    n=int(input())
    if(tong(n)%10==0 and check1(n)):
        print('YES')
    else:
        print('NO')
