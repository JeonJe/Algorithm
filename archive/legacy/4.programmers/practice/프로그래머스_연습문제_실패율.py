def solution(N, stages):
    answer, temp = [], []
    count_temp = [0] * (N + 2)
    for i in range(1,N+2):
        count_temp[i] = stages.count(i)

    total = sum(count_temp)
    for i in range(1,N+1):
        temp.append((count_temp[i]/total,i))
        total -= count_temp[i]

    temp.sort(key=lambda x : (-x[0],x[1] ))
    for _,k in temp:
        answer.append(k)

    return answer

# N = 5
N = 4
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = 	[4,4,4,4,4]
print(solution(N,stages))