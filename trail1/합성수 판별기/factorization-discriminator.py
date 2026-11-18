import sys
# 합성수 : c, 아니면 n
n=int(input())
for i in range(2,n):
    if (n%i)==0:
        print('C')
        sys.exit()
    
print('N')
