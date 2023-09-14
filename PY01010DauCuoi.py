t=int(input())
while(t>0):
    n=int(input())
    m=n%100
    tmp=0
    while(n>0):
        tmp=tmp*10+n%10
        n//=10
    tong=tmp%10
    tmp//=10
    tong=tong*10+tmp%10

    if(tong==m): print('YES')
    else: print('NO')


    t-=1