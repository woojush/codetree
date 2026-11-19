n=int(input())
student_score=list()
score_total=0
cnt=0
for i in range(n):
    student_score=list(map(int, input().split()))
    score_total=sum(student_score)
    if ((score_total/4)>=60):
        cnt+=1
        print("pass")
    else:
        print("fail")
print(cnt)