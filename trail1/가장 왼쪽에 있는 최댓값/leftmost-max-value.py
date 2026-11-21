n = int(input())
a = list(map(int, input().split()))

# Please write your code here.




max_idx=n
while(max_idx>0):
    max=0
    for i in range(max_idx):
        if a[i]>max:
            max=a[i]
            max_idx=i           
    print(max_idx+1,end=" ")
        
        