from math import *
t=int(input())
for _ in range(t):
    s=input()
    ok=1
    for i in range(2,len(s)):
        if(s[i]!=s[i-2]):
            ok=0;
            break;
    if(ok==1): print('YES')
    else: print('NO')
