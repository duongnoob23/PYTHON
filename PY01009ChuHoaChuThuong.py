s=input()
le=0
for i in s:
    if i.islower():
        le+=1
if(le > len(s)-le):
    print(s.lower())
else:
    print(s.upper())