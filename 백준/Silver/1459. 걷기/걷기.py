x,y,t1,t2 = list(map(int,input().split()))
time = 0
#블록2번이 대각선 1번보다 작거나 같으면 블록으로 다님
if 2*t1 <= t2:
    time += t1 * x + t1 * y 

else:
    close = min(x,y)
    far = max(x,y)
    diff = far - close 
    time += close * t2 
    
    if t2 < t1:
        q, r = diff // 2, diff % 2
        time += q * t2*2
        time += r * t1
    else:
        time += diff * t1

print(time)