import heapq

k, n = map(int,input().split())
primes = list(map(int,input().split()))
primes.sort()
res =[]

for i in primes:
    heapq.heappush(res,i)

for i in range(n):
    m = heapq.heappop(res)

    for k in range(len(primes)):
        new_num = m * primes[k]
        heapq.heappush(res,new_num)

        if m % primes[k] == 0:
            break 

print(m)


