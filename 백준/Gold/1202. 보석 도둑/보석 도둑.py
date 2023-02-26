import heapq
from collections import deque

N, K = map(int,input().split())

cnt = 0
i = 0

que = []
jewels = [list(map(int,input().split())) for _ in range(N) ]
bag_weight = [int(input()) for _ in range(K) ]

#가방 무게로 오름차순 정렬
bag_weight.sort()

for weight,value in jewels:
    heapq.heappush(que,(weight,value))

temp = []

for i in range(len(bag_weight)):

    #보석 중 제일 가벼운 보석이 현재 가방 무게 보다 무거움
    # if que[0][0] > bag_weight[i] and temp:
    #     continue 

    #보석에서 현재 가방보다 가벼운 보석들을 찾아서 temp에 넣음
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