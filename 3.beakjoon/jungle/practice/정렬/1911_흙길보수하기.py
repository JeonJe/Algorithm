import math 
N,L = map(int,input().split())

pools = [ list(map(int,input().split())) for _ in range(N)]
pools.sort(key=lambda x : x[0])

last_plank_point = 0
cnt = 0

for i in range(len(pools)):
    cur_pool_start, cur_pool_end = pools[i][0], pools[i][1]
    
    #기존 널빤지가 물웅덩이를 덮을 수 있는 경우 
    if last_plank_point > cur_pool_end:
        continue
    
    #기존 널빤지가 물웅덩이 시작 후 일부분을 덮을 수 있는 경우 
    if last_plank_point > cur_pool_start:
        #널빤지가 커버하는 마지막 부분으로 시작지점 이동
        cur_pool_start = last_plank_point
        
    #현재 물웅덩이를 덮기 위해 필요한 널판지 개수 
    need = math.ceil((cur_pool_end - cur_pool_start)/ L)
    cnt += need
    #마지막 널빤지 위치는 현재 널빤지 시작지점 + (널빤지 개수 * 길이 )
    last_plank_point = cur_pool_start + (need * L)
print(cnt)

