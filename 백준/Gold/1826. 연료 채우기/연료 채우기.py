from collections import deque 
import heapq

n = int(input())

stations = [ list(map(int,input().split())) for _ in range(n) ]
stations.sort()
destination, fuel = map(int,input().split())

#남은 연료를 사용하여 최대로 멀리갈 수 있는거리
max_reach = fuel 
que = deque()
for point, amount in stations:
    que.append((point,amount))

#현재 위치
cur = 0
answer = 0
max_heap = []
while max_reach < destination:
    #가지고 있는 연료를 사용해서 도달할 수 있는 주유소 중 가장 연료를 많이 받을 수 있는 주유소의 위치와 양을 찾는다

    while que:
        if que[0][0] <= max_reach:
            cur_station_point, cur_station_amount = que.popleft()
            heapq.heappush(max_heap,(-cur_station_amount,cur_station_point))
        else:
            break

    if max_heap:
        pick_amount, pick_point = heapq.heappop(max_heap)
        pick_amount *= -1
        
        fuel -= pick_point - cur
        cur = pick_point
        fuel += pick_amount
        max_reach = cur+fuel

        answer += 1
    else:
      answer = -1
      break

print(answer)

