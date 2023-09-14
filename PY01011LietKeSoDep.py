def TN(a):
    tmp=0
    tmp1=a
    while(a>0):
        tmp=tmp*10+a%10
        a//=10
    if(tmp==tmp1): return 1
    else: return 0

def check(a):
    dem=0
    while( a >  0):
        tmp=a%10
        if(tmp!=0 and tmp!=2 and tmp!=4 and tmp!=6 and tmp!=8):
            return 0
        dem+=1
        a//=10
    if(dem%2==0): return 1
    return 0


t=int(input())
for _ in range(t):
    n=int(input())
    for x in range(22,n,1):
        if(check(x) and TN(x)):
            print(x,end=' ')
    print()


