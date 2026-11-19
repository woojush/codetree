import sys
for i in range(5):
    a=int(input())
    if (a%3): # 만약 3으로 나누어 떨어지지 않으면.
        print(0)
        sys.exit()
print(1)