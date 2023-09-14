t=int(input())
for _ in range(t):
    s=input()
    min1=-1e9
    tong=0
    for i in range(len(s)):
        if(s[i].isdigit()):
            tong=tong*10+int(s[i])
        else:
            if(i!=0 and s[i-1].isdigit() ):
                min1=max(tong,min1)
                tong=0
    if tong!=0: min1=max(tong,min1)
    print(min1)