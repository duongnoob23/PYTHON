from math import *
while(True):
    n=int(input())
    if (n == 0): break
    dem=0
    while(n!=1):
        if(n%2==0):
            n//=2
            dem+=1
        else:
            n=n*3+1
            dem+=1
    print(dem+1)
'''
1 3 5 9
2 2 4 7
0 2 3 5
2 1 2 5
1 1 3 3
0 2 0 2
2 2 2 2

4 3 2 1
1 1 1 0
0 0 1 1
0 1 0 1
1 1 1 1
'''