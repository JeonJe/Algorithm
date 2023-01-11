import heapq

N = int(input())
que = []
nums = [ int(input()) for _ in range(N) ]

for num in nums:
    heapq.heappush(que,(num))

cnt = 0
while len(que) >=2 :
    f = heapq.heappop(que)
    s = heapq.heappop(que)
    cnt += f + s 
    heapq.heappush(que,f+s)



print(cnt)

