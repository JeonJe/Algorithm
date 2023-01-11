n = int(input())
k = int(input())

left = 0
right = k 

# 이진탐색으로 인덱스가 들어갈 위치를 찾는다.
def lower_bound(left, right, target):

    while left < right:
        mid = (left + right) // 2
        cnt = 0

        for i in range(1,n+1):
            cnt += min(mid//i, n)

        if cnt < target:
            left = mid + 1
        else:
            right = mid
    print(right)

lower_bound(left,right, k)