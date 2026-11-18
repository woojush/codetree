# 1~n까지의 숫자 중 3의 배수를 출력

n=int(input())
i=1
while(i<=n):
    if (i%3==0):
        print(i,end=" ")
    i+=1