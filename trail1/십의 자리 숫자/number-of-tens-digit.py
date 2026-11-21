arr=list(map(int,input().split()))
new_arr=list()
cnt = [0 for _ in range(9)]
for elem in arr:
    if elem==0:
        break
    new_arr.append(elem//10)

for i in new_arr:
    if i!=0:
        cnt[i-1]+=1
        
for i in range(9):
    print(f"{i+1} - {cnt[i]}")

# 십의자리로 떼어냄
# 십의자리를 카운트
