# 수열 A의 원소 개수 : N1
# 수열 B의 원소 개수 : N2

#수열 B가 수열 A의 연속부분수열인지 판단하라.

# 연속부분수열이란?
    # A=[1,5,2,6] 에 대해 B가 [5,2]이면 연속부분수열.
    # B가 [5,6]이면 연속부분수열 아님.

# 연속부분수열을 판단하기 위해서는 어떻게 해야할까?
# A와 B가 제공된 상황이라고 가정하자.

# B[0]이 A의 몇번째 인덱스에 있는지 index() 함수를 활용하여 찾는다. (그 인덱스를 idx라 하자.)
# B의 원소 개수만큼 for문을 돌린다. ex N2=3 -> for i in range(1,3):
# A[idx+i]=B[i]가 아닌 경우, print("No") & sys.exit()
n1,n2=map(int,input().split())

A=input().split()
B=input().split()
found=False
for i in range(0,n1-n2+1):
    if A[i:i+n2]==B:
        found=True
        break
print("Yes" if found else "No")

