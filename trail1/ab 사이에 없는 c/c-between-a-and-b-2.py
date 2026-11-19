a=False
a,b,c=map(int, input().split())
for i in range(a,b+1):
    if (i%c==0):
        a=False
        break
    else:
        a=True
if (a):
    print("YES")
else:
    print("NO")
        
