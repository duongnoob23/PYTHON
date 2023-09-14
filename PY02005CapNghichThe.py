t=int(input())
a=list(map(int,input().split()))
dem=0
for i in range(0,t-1):
    for j in range(i+1,t):
        if(a[i]>a[j]):
            dem+=1
print(dem)