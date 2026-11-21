n=int(input())
arr=list(map(int, input().split()))

min=100
for i in range(1,n):
    if arr[i]-arr[i-1]<min:
        min=arr[i]-arr[i-1]
print(min)