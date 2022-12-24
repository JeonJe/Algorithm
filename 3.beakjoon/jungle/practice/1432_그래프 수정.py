import heapq 

n = int(input())

#각 노드에 연결된 간선 정보를 담기 위한 연결리스트
graph = [ [] for _ in range(n+1) ]
outdegree = [0]*(n+1)
result = [0]*(n+1)

for i in range(1,n+1):
    infos = list(map(int,input()))

    for idx, val in enumerate(infos):
        if val == 1:
            graph[idx + 1].append(i)
            outdegree[i] += 1

def topology_sort(n):
    #큐에 여러노드가 있을 경우 인덱스가 큰 노드를 먼저 큐에서 빼내야함
    #답이 여러개 일 경우 사전 순으로 제일 앞서는 것 출력
    heap = []

    for i in range(1, n+1):
        if outdegree[i] == 0:
            heapq.heappush(heap, -i)
    
    while heap:
        # 인덱스가 가장 큰 노드를 꺼내고
        #해당 노드와 연결된 노드들의 차수를 뺀다
        #큐에서 빼낸 노드번호를 인덱스로 result리스트에 저장
        now = -heapq.heappop(heap)
        result[now] = n

        for adj in graph[now]:
            outdegree[adj] -= 1
            if outdegree[adj] == 0:
                heapq.heappush(heap, -adj)
        
        n -= 1

topology_sort(n)

#그래프 번호를 수정할 수 없는 노드가 2개 이상이라면 -1
#사이클이 돌려면 최소 3개의 노드가 서로 가리키고 있어야하는데
#그러면 2개 이상의 노드는 진출 차수가 0이 될 수 없다.

if result.count(0) > 2:
    print(-1)
else:
    print(' '.join(map(str,result[1:])))
    


