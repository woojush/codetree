arr=list(map(int, input().split()))
cnt=[0 for _ in range(10)]
for i in range(10):
    cnt[arr[i]-1]+=1
    
for i in range(6):
    print(f"{i+1} - {cnt[i]}")