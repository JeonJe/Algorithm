import heapq

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


