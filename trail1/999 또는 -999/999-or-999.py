arr=list(map(int, input().split()))
max=min=arr[0]
for elem in arr:
    if elem==999 or elem==-999:
        break
    if elem>max:
        max=elem
    if elem<min:
        min=elem
print (max,min)