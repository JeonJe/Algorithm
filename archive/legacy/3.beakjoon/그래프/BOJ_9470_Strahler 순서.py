from collections import deque

t = int(input())

def topology_sort():
    num_same_degree = [0] *(m+1)
    order = [0] * (m+1)
    que = deque()
    ans = 0

    for i in range(1,len(in_degree)):
        #들어오는 차수가 0인 노드는 강의 근원
        if in_degree[i] == 0:
            que.append(i)
            #순서
            order[i] = 1
            #i로 들어오는 in_degree개수
            num_same_degree[i] += 1
    
    while que:
        cur = que.popleft()
        #cur로 들어오는 in_degree 개수가 2개 이상이면 순서 +1
        if num_same_degree[cur] >= 2:
            order[cur] += 1
        ans = max(ans, order[cur])

        #현재 노드와 연결되어 있는 주변노드 방문
        for adj in graph[cur]:
            
            #cur-> adj로 가는 노드의 수를 제외한다
            in_degree[adj] -= 1

            if in_degree[adj] == 0:
                #adj로 가는 모든 간선을 확인하였으므로 
                #이제 adj를 확인하기 위해 큐에 삽입한다
                que.append(adj)
            
            #현재노드와 adj 노드의 order같으면 같은 order의 개수를 증가
            if order[cur] == order[adj]:
                num_same_degree[adj] += 1
            #더 큰 순서를 가진 것으로 증가 
            #adj가 더 크면 num_same_degree는 유지
            #새로운 경로인 cur-> adj가 더 크면, order를 업데이트해주고
            #num_same_degree 수를 1로 초기화한다.
            elif (order[adj] < order[cur]):
                order[adj] = order[cur]
                num_same_degree[adj] = 1
    return ans



for T in range(t):
    k, m, p = map(int,input().split())
    graph = [ [] for _ in range(m+1) ]
    in_degree = [0] * (m+1)    
    
    for _ in range(p):
        fr, to = map(int,input().split())
        graph[fr].append(to)
        in_degree[to] += 1
    
    max_value = topology_sort()
    print(T+1, max_value)