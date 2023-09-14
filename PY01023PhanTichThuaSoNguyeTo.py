import math
t=int(input())
for _ in range(t):
    n=int(input())
    print(1,end=' ' )
    print('*',end=' ')
    for i in range(2,math.isqrt(n)):
        dem=0
        while(n%i==0):
            dem+=1
            n//=i
            if(n%i!=0):
                print(i,end='')
                print('^',end='')
                print(dem,end=' ')
                if(n!=1):
                    print('*', end=' ')
                else:
                    print()
    if(n!=1):
        print(n, end='')
        print('^', end='')
        print(1,)
