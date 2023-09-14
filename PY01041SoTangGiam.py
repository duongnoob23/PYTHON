t=int(input())
for _ in range(t):
    s=input()
    a=list(int(i) for i in s)
    dem=1
    ok=0;
    if(len(a)<3):
        print('NO')
    else:
        for i in range(1,len(a)):
            if(a[i]>a[i-1] and ok==0):
                dem+=1
            elif(a[i] < a[i-1] and ok==1):
                dem+=1
            elif(a[i] < a[i-1] and ok==0):
                ok=1
                dem+=1

        if(dem==len(a)): print("YES")
        else: print('NO')





