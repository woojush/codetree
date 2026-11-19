n=int(input())
line=0
for i in range(2*n-1,0,-2):
    print(" "*line,end="")
    print("* "*i)
    line+=2