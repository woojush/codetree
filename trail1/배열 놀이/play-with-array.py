size_of_N, Q=map(int, input().split())
N=list(map(int, input().split()))

arr=[0]*Q
for i in range(Q):
    arr=list(map(int,input().split(" ")))
    if arr[0]==3:
        for i in range(arr[1]-1, arr[2]): 
            print(N[i],end=" ")
    elif arr[0]==1:
       print(N[arr[1]-1],end="") 
    else:
        if arr[1] in N:
            idx=N.index(arr[1])+1
        else:
            idx=0
        print(idx,end="")
    print("\n",end="")
    
    
