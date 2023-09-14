

a,k,n=map(int,input().split())
ok=0
for i in range(0,n+1,k):
    if(i-a>0):
        ok=1
        print(i-a,end=' ')
if ok==0: print(-1)