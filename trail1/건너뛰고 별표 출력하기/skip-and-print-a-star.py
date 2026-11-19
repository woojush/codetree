n=int(input())
for i in range(1,n+1):
    print("*"*i)
    print("\n",end="")
for j in range(n-1,0,-1):
    print("*"*j)
    print("\n",end="")