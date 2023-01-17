import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))


# 이진탐색으로 인덱스가 들어갈 위치를 찾는다.
def lower_bound(start, end, num):
    while start < end:
        mid = (start + end) // 2

        if tmp[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end

tmp = []
index = [[0, 0] for _ in range(n)]

tmp.append(arr[0])
#0번째 인자의 위치, 인덱스 값
index[0][1] = arr[0] 

for i in range(1,len(arr)):
    num = arr[i]
    index[i][1] = num

    # if len(tmp) == 0:
    #     tmp.append(num)
    #     continue

    if tmp[-1] < num:
        index[i][0] = len(tmp)
        tmp.append(num)
    else:
        idx = lower_bound(0, len(tmp)-1, num)
        index[i][0] = idx
        tmp[idx] = num


answer = []
order = len(tmp)-1
for i in range(len(index)-1, -1, -1):
    if order == -1:
        break

    if order == index[i][0]:
        answer.append(index[i][1])
        order -= 1

print(len(tmp))
print(*answer[::-1])
    