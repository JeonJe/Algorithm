import sys

# sys.stdin = open("input.txt",'r') 

def dfs(level, sum_point, spend_time):
    global res
    #문제푸는 총 시간이 제한시간보다 크면 계산하지 않음
    if spend_time > M:
        return 
    if level == N:
        if sum_point> res:
            res = sum_point
    
    else:
        #다음 문제를 푸는 경우 
        dfs(level+1, sum_point + points[level], spend_time + times[level])
        #다음 문제를 풀지 않은 경우
        dfs(level+1, sum_point, spend_time)
        
N,M = map(int,input().split())
#N = 문제개수, M = 제한시간
points =[]
times =[]


for _ in range(N):
    point,time= map(int,input().split())
    points.append(point)
    times.append(time)
   
res = -sys.maxsize -1
    # print(points,times)
dfs(0,0,0)
print(res)