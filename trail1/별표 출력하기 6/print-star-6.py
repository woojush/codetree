n = int(input())


for i in range(n):  #0
    print("  " * i, end="")  # 0
    print("* " * (2 * n - 2 * i - 1))  # 2+1
for j in range(n - 2, -1, -1):
    print("  " * j, end="")
    print("* " * (2 * n - 2 * j - 1))
