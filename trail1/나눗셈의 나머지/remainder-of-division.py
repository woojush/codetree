A,B=map(int,input().split())
remain=[0]*10
while(A>1): 
    remain[A%B]+=1
    A=A//B
sum=0
for i in range(10):
    sum+=remain[i]**2
print(sum)