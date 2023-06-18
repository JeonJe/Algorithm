x,y,t1,t2 = list(map(int,input().split()))
time = 0
#블록2번이 대각선 1번보다 작거나 같으면 블록으로 다님
if 2*t1 <= t2:
    time += t1 * x + t1 * y 

else:
    close = min(x,y)
    far = max(x,y)
    diff = far - close 
    #대각선으로 갈 수 있을만큼 가는게 이득
    time += close * t2 
    
    #나머지에 대해서 어떻게 갈까 고민중 대각으로 더 갈수있나?
    #대각선 1번이 블록 1번보다 더 이득일 경우 끝까지 대각선으로 가봄 
    #대각2번으로 블록 한 방향2칸 이동 가능, 나머지는 블록이동
    if t2 < t1:
        q, r = diff // 2, diff % 2
        time += q * t2*2
        time += r * t1
    #그냥 블록으로 다 이동해버렷
    else:
        time += diff * t1

print(time)