import sys
a=[0]*5
for i in range(5):
    a[i]=int(input())
    if (a[i]%3): # 만약 3으로 나누어 떨어지지 않으면.
        print(0)
        sys.exit()
print(1)