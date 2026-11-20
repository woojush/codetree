

rank_cnt=[0]*4
for i in range(3):
    cold,temp=map(str, input().split())
    if cold=='Y':
        if int(temp)>=37:
            rank_cnt[0]+=1
        else:
            rank_cnt[2]+=1
    else:
        if int(temp)>=37:
            rank_cnt[1]+=1
        else:
            rank_cnt[3]+=1

for i in range(4):
    print(rank_cnt[i],end=" ")
if rank_cnt[0]>=2:
    print ("E", end="")