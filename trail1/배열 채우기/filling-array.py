arr=list(map(int, input().split()))
if 0 in arr:
    idx=arr.index(0)
    for i in arr[idx-1::-1]:
        print(i,end=" ")
else:
    for i in arr[::-1]:
        print(i,end=" ")
