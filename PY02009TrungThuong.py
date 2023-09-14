t=int(input())
for _ in range(t):
    n=int(input())
    a=[0]*(10**3+1)
    res=0
    number=0
    for i in range(n):
        m=int(input())
        a[m]+=1

    for i in range(0,10**3+1):
         if a[i]>res:
            res=a[i]
            number=i
    print(number)
