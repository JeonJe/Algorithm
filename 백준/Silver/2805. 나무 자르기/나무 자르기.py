import sys
N, M = map(int,input().split())

trees = list(map(int,sys.stdin.readline().split()))

left = 0
right = max(trees)

#나무 높이 
def check(x, M):
    sum = 0
    for tree in trees:
        if tree >  x:
            sum += tree - x 
    if sum >= M:
        return True
    else:
        return False

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid,M): left = mid 
    else: right = mid

print(left)
