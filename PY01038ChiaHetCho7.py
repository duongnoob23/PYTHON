from math import *

t=int(input())
for _ in range(t):
    ok=1
    n=int(input())
    for i in range(1000):
        if n % 7 ==0:
            ok=1
            print(n);
            break;
        nr=int( str(n)[::-1] )
        n+=nr
    if(ok==0): print(-1)