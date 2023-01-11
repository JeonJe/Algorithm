import heapq
from collections import deque

N, K = map(int,input().split())

cnt = 0
que = []
temp = []

jewels = [list(map(int,input().split())) for _ in range(N) ]
bag_weight = [int(input()) for _ in range(K) ]
bag_weight.sort()

for weight,value in jewels:
    heapq.heappush(que,(weight,value))

for i in range(len(bag_weight)):

    while len(que) > 0:
        j_weight, j_value = que[0][0], que[0][1]

        if j_weight <= bag_weight[i]:
            heapq.heappop(que)
            heapq.heappush(temp,(-j_value,j_weight))
        else:
            break

    if len(temp) > 0 and temp[0][1] <= bag_weight[i]:
        v, w = heapq.heappop(temp)
        v *= -1
        cnt+= v

print(cnt)