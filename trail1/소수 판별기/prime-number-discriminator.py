import sys, math
N=int(input())
# 소수 : P, 합성수 : C

for i in range(2,int(math.sqrt(N))+1):
    if (N%i==0):
        print("C")
        sys.exit()
print("P")