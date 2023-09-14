from math import *

def nto(a):
    if(a<2): return False
    for i in range(2,isqrt(a),1):
        if(a%i==0): return False
    return True



t=int(input())
for _ in range(t):
    s=input()
    tong=0
    for i in range(len(s)-4,len(s),1):
        tong=tong*10+int(s[i])
    if(nto(tong)): print('YES')
    else: print('NO')
