import heapq 

n = int(input())
seq = [list(map(int,input().split())) for _ in range(n)]
seq.sort(key=lambda x : (x[1],x[2]))

answer = 0
heap = []

for i in range(len(seq)):
    cur_start, cur_end = seq[i][1], seq[i][2]

    if heap:
        #가장 일찍 끝나는 강의보다 더 늦게 시작하는 강의이면 그 강의실에서 강의 진행 가능
        if cur_start >= heap[0][0]:
            heapq.heappop(heap)
        
    heapq.heappush(heap,(cur_end,cur_start))
    answer = max(answer, len(heap))
        

print(answer)

