
import heapq

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

def solution(k, score):
    answer = []
    que = []
    for i in range(len(score)):
        if len(que) < k:
            heapq.heappush(que, score[i])
        else:
            if score[i] > que[0]:
                heapq.heappop(que)
                heapq.heappush(que, score[i])
        answer.append(que[0])

    return answer


print(solution(k,score))