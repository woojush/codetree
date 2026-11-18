import sys
a,b=map(int, input().split())
for i in range(a,b):
    if (1920%i==0&2880%i==0):
        print(1)
        sys.exit()

print(0)
