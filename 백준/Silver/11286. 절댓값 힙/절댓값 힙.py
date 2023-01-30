import heapq 

n = int(input())
data = [int(input()) for _ in range(n)]
que = []

for d in data:
    #pop
    if d == 0:
        if que:
            print(heapq.heappop(que)[1])
        else:
            print(0)
    else:
        heapq.heappush(que,(abs(d),d))

