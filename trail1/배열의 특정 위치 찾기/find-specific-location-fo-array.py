arr=list(map(int,input().split()))
even_array=arr[1::2]
array3=arr[2::3]
print(f"{sum(even_array)} {sum(array3)/len(array3):.1f}")
    