t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(b==1):
        if(a>19): print('Bao Binh')
        else: print('Ma Ket')
    elif(b==2):
        if(a>18): print('Song Ngu')
        else: print('Bao Binh')
    elif(b==3):
        if(a>20): print('Bach Duong')
        else: print('Song Ngu')
    elif(b==4):
        if(a>19): print('Kim Nguu')
        else: print('Bach Duong')
    elif(b==5):
        if(a>20): print('Song Tu')
        else: print('Kim Nguu')
    elif(b==6):
        if(a>20): print('Cu Giai')
        else: print('Song Tu')
    elif(b==7):
        if(a>22): print('Su Tu')
        else: print('Cu Giai')
    elif(b==8):
        if(a>22): print('Xu Nu')
        else: print('Su Tu')
    elif(b==9):
        if(a>22): print('Thien Binh')
        else: print('Xu Nu')
    elif(b==10):
        if(a>22): print('Thien Yet')
        else: print('Thien Binh')
    elif(b==11):
        if(a>22): print('Nhan Ma')
        else: print('Thien Yet')
    else:
        if(a>21): print('Ma Ket')
        else: print('Nhan Ma')
