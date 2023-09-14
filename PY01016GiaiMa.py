t=int(input())
for _ in range(t):
    s=input()
    dem=0
    chu=""
    for i in range(len(s)):
        if(s[i].isalpha()):
            chu=s[i]
        else:
            dem=int(s[i])
            for i in range(1,dem+1):
                print(chu)

