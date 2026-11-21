n=int(input())
cnt=[0 for _ in range(9)]
arr=list(map(int, input().split(" ")))
for i in arr: # 1
    cnt[i-1]+=1
for i in range(9):
    print(cnt[i])