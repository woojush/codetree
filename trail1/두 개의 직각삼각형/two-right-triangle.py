n=int(input())
for i in range(n):
    print("*"*(n-i),end="")
    if (i):
        print("  "*i,end="")
    print("*"*(n-i))
    