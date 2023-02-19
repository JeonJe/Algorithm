def solution(N, stages):
    answer, temp = [], []
    count_temp = [0] * (N + 2)
    for i in range(1,N+2):
        count_temp[i] = stages.count(i)

    total = sum(count_temp)
    
        
    for i in range(1,N+1):
        if total == 0:
            temp.append((0,i))
        else:
            temp.append((count_temp[i]/total,i))
            total -= count_temp[i]

    temp.sort(key=lambda x : (-x[0],x[1] ))
    for _,k in temp:
        answer.append(k)

    return answer