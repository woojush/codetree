a1,a2=map(int,input().split())
arr=[a1,a2]
for i in range(2,10):
    arr.append(2*arr[i-2]+arr[i-1])

for i in range(10):
    print(arr[i],end=" ")
