t=int(input())
while(t>0):
    n=int(input())
    dem4=dem7=dem=0
    while(n>0):
        if n%10==4: dem4+=1
        if n%10==7: dem7+=1
        dem+=1
        n//=10

    if dem4+dem7==dem: print("YES")
    else: print("NO")

    t-=1
