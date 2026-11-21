n = int(input())
a = list(map(int, input().split()))
#N개의 정수 내림차순 정렬, 첫번째 두번째 정수를 출력하라.
# Please write your code here.
a.sort(reverse=True)
print(a[0], a[1])