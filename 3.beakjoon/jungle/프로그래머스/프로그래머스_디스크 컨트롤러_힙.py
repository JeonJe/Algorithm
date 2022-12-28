from collections import deque 

def solution(jobs):
    time = 0
    que = deque()
    total_waiting = 0
    
    for start, worktime in jobs:
        que.append((worktime,start))
    #작은 일 시간 기준 
 
    que =  sorted(que, key=lambda x : x[0])
    while que:
        
        #요청시간이 현재시간보다 나중이라면
        i = 0
        while que[i][1] > time and i < len(que)-1:
            i += 1
        #현재 가장빨리 처리할 수 있는 찾았을 때 
        if que[i][1] <= time:
            time += que[i][0]
            total_waiting += time - que[i][1]
            que.remove(que[i])
        else:
        #처리 할 수 있는 일이 없을 때, 시간만 증가 
            time += 1

    answer = total_waiting // len(jobs)
    return answer





jobs = [[0, 3], [1, 9], [2, 6], [10000000000000000000,3 ]]
print(solution(jobs))