from math import *

t=int(input())
for _ in range(t):
    s=input()
    sum1 = str( sum(int(i) for i in s) )

    if(len(sum1)>1 and sum1==sum1[::-1]): print('YES')
    else: print('NO')