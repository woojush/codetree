arr=list(map(int, input().split()))

if 0 in arr:
    i=0
    sum=0
    while(arr[i]!=0):
        sum+=arr[i]
        i+=1
    print(f"{sum} {sum/i:.1f}")

else:
    sum=sum(arr)
    print(f"{sum} {sum/len(arr):.1f}")