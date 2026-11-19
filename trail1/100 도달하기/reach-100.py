from getopt import do_longs

n=int(input())
arr=[1,n]
i=2
print(arr[0], arr[1],end=" ")
while True:
    arr.append(arr[i-1]+arr[i-2])
    print(arr[i], end=" ")
    if arr[i]>100:
        break
    i+=1