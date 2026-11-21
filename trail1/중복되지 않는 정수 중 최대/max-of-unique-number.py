n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

#중복하지 않은 수 중 최대값을 찾아라.
#모든 수가 다 중복한다면, -1을 출력하라.

# 딕셔너리로, 수와 등장횟수를 적는다.
# value !=1인 key를 리스트에 넣는다.
# key를 담은 리스트를 정렬 후 최대값 출력한다.
# 애초에 딕셔너리가 비어있다면, -1을 출력한다.

arr=list()
for elem in nums:
    if nums.count(elem)==1:
        arr.append(elem)
if len(arr)==0:
    print(-1)
else:
    arr.sort()
    print(arr[-1])