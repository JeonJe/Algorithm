
n = int(input())

times = [ list(map(int,input().split())) for _ in range(n)]
times.sort(key=lambda x : (x[1],x[0]))

res = 0
last = 0

for i in range(len(times)):
    start, end = times[i][0], times[i][1]

    if last <= start:
        res += 1
        last = end 

print(res)