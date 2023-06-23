N, M = map(int,input().split())
seq = list(map(int,input().split()))

left = 0
right = (max(seq)*N)+1

def find_last_persion(time):
    before_end = time - 1
    #마지막 1초전까지 몇 명 탈수있었는지?
    t = 0
    for s in seq:
        t += (before_end // s + 1)

    #time 시간에 타야하는 인원 수 
    diff = N - t
        
    last = 1
    while diff:
        for i in range(len(seq)):
            if  time % seq[i] == 0:
                last = i+1
                diff -= 1
                if diff == 0:
                    break
    return last
    
    

def check(time):

    #time이란 시간동안 각 놀이기구에 탈 수 있는 사람의 합을 구해서
    #M보다 크면 모든 아이들이 해당 시간안에 놀이기구를 탈 수 있음 
    t = 0
    for s in seq:
        t += (time // s) + 1
    
    if t >= N:
        return True
    else:
        return False
    

if N <= M:
    print(N)

else:
    while left + 1 < right:
        mid = left + (right - left) // 2

        if check(mid):
            right = mid
        else:
            left = mid
        
    #최소 시간(right)에서 마지막에 타는 사람이 탈 놀이기구는 몇 번째 놀이기구?
    print(find_last_persion(right))


