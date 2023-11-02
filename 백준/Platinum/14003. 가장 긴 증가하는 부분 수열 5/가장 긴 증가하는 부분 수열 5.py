import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))

def lower_bound(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if LIS[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

LIS = []
LIS.append(seq[0])
#i번째 수열의 LIS 로 들어갈 때 index위치와 값 
index_and_value = [ [0, 0] for _ in range(n)]
index_and_value[0][1] = seq[0]

for i in range(1, len(seq)):
    current_num = seq[i]
    index_and_value[i][1] = current_num

    #LIS의 마지막 수열보다 크기가 클 경우, LIS뒤에 넣고, idx 위치는 LIS 길이
    if current_num > LIS[-1]:
        index_and_value[i][0] = len(LIS)
        LIS.append(current_num)
    else:
    #lower bound로 current_num이 들어갈 적절한 위치를 찾음
        idx = lower_bound(0, len(LIS)-1, current_num)
        index_and_value[i][0] = idx
        LIS[idx] = current_num

answer = []
order = len(LIS) - 1

for i in range(len(index_and_value)-1,-1,-1):
    if order == -1:
        break
    if order  == index_and_value[i][0]:
        answer.append(index_and_value[i][1])
        order -= 1

print(len(LIS))
print(*answer[::-1])
