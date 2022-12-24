
# 한시간 피로도 A, 일량 B, 일안할때 피로도C 감소, 피로도 최대치 M
A,B,C,M = list(map(int,input().split()))

work = 0
cur_tired = 0 
time = 0
while time < 24:
    #일을 할 피로도가 있으면 일 시작 

    if cur_tired + A <= M:
        cur_tired += A 
        work += B
    #일 못하면 쉬기 
    else:
        cur_tired = cur_tired - C 
        cur_tired = max(cur_tired, 0)

    time += 1

print(work)