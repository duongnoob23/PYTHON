from math import *

def nto(a):
    if(a<2): return False
    for i in range(2,isqrt(a),1):
        if(a%i==0): return False
    return True

t=int(input())
for _ in range(t):
    s=input()
    dem=0
    for i in range(len(s)):
        if(s[i]=='2' or s[i]=='3' or s[i]=='7' or s[i]=='5'):
            dem+=1
    if(nto(len(s)) and dem>(len(s)-dem)):
        print('YES')
    else:
        print('NO')