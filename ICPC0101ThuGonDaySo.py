from math import *

n=int(input())
a=list(map(int,input().split()))

i=0
while(i<len(a)-1):
    if( (a[i]+a[i+1])%2==0 ):
        a.pop(i+1)
        a.pop(i)
        if(i>=1):
            i-=1
    else:
        i+=1
print(len(a))

'''
0 1 2 3 4 5 6 7 8 9
5 4 

7
1 3 2 4 1 3 2

4
1 3 2 4

5
1 3 2 1 3

7
2 3 2 3 1 4 5
'''