import math
satisfied=True
n=int(input()) # 8
for i in range(2, n+1): # 2 3 4 5 6 7 8
    for j in range(2, int(math.sqrt(i)+1)): # 2~루트2+1->2 
        if (i%j==0): # 소수가 아님 
           satisfied= False
           break
        else : # 소수
            satisfied=True
    if (satisfied==True):
        print(i,end=" ")

    