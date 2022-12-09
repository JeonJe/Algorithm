import math
N,L = map(int,input().split())

pools = [ list(map(int,input().split())) for _ in range(N)]
pools.sort(key=lambda x : x[0])
cnt = 0

prev_end = 0
cnt = 0

for i in range(len(pools)):
    cur_start, cur_end = pools[i][0], pools[i][1]
    if prev_end > cur_end:
        continue
    if prev_end > cur_start :
        cur_start = prev_end

    prev_end = cur_start
    need = math.ceil((cur_end - cur_start)/ L)
    cnt += need
    prev_end += need * L

print(cnt)