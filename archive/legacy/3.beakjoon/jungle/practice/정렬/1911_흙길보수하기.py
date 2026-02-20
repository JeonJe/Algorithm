
N, L = map(int,input().split())

pools = [ list(map(int,input().split())) for _ in range(N)]

pools.sort()
last_plank_point = -1
res = 0
for i in range(len(pools)):
    pool_start, pool_end = pools[i][0], pools[i][1]

    if last_plank_point > pool_end:
        continue

    if last_plank_point > pool_start:
        pool_start = last_plank_point
    
    
    need = pool_end - pool_start
    if need % L == 0:
        need = need // L 
    else:
        need = (need // L) + 1
    res+= need 
    last_plank_point = pool_start + (need * L)


print(res)

