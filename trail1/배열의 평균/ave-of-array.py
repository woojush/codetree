arr_2D=[[0 for col in range(4)] for row in range(2)]
for i in range(2):
        arr=(list(map(int, input().split())))
        arr_2D[i]=arr
for i in range(2):
    sum=0
    for j in range(4):
        sum+=arr_2D[i][j]
    print(f"{sum/4:.1f}",end=" ")
print()
total=0

for i in range(4):
    sum=0
    for j in range(2):
        sum+=arr_2D[j][i]
    total+=sum
    print(f"{sum/2:.1f}",end=" ")
print()
print(f"{total/8:.1f}")
