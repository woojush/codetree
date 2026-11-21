import sys
n = int(input())
if n==1:
    print(0)
    sys.exit()
price = list(map(int, input().split()))


right_idx=n-1
arr=list()
while(right_idx>0):
    arr.append(price[right_idx]-min(price[:right_idx]))
    right_idx-=1
if (max(arr)>0):
    print(max(arr))
else:
    print(0)