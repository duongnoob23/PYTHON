t=int(input())
for _ in range(t):
    s=input()
    a=list( i for i in s)
    dem=0
    for i in a:
        if(i=='0' or i=='1' or i=='2'):
            dem+=1
    if(dem==len(a)): print('YES')
    else: print('NO')