arr=list(map(int,input().split()))
sum,cnt2=0,0
for elem in arr:
    if elem==0:
        break
    if elem%2==0:
        cnt2+=1
        sum+=elem
print(cnt2, sum)