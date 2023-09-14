
import math
def check(n):
    while(n>10):

        if(n%10 < n//10%10):
            return False
        n//=10
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    if(check(n)):
        print('YES')
    else:
        print('NO')