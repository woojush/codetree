arr=list(map(int,input().split()))
under_arr=list()
over_arr=list()
for elem in arr:
    if elem>500:
        over_arr.append(elem)
    else:
        under_arr.append(elem)
print(max(under_arr), min(over_arr))
