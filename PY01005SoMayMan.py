n=int(input())
dem4=0
dem7=0
while(n>0):
    t=n%10
    if t==4:  dem4+=1
    if t==7:   dem7+=1
    n//=10


if(dem4+dem7==4 or dem4+dem7==7):
    print("YES")
else:
    print("NO")