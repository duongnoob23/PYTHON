t=int(input())
while(t>0):
    x,y,z=map(float,input().split())
    dem=0
    while(x<z):
        x=x+x*y//100
        dem+=1

    print(dem)

    t-=1