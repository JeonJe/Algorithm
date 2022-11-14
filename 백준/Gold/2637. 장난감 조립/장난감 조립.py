from collections import deque

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1) ]
in_degree = [0]*(n+1)

def topological_sort():
    need_parts =[ [0]*(n+1) for _ in range(n+1) ]
    que = deque()
    temp = 0

    for i in range(1,n+1):
        #기본부품
        if in_degree[i] == 0:
            que.append(i)

    while que:
        p = que.popleft()
        # p는 adj를 만들기 위해 num만큼의 개수가 필요 
        for adj,num in graph[p]:
            #기본부품
            #중간부품을 만들기 위해 필요한 p가 기본제품이면
            # if p <= temp:
            if need_parts[p].count(0) == n+1:
                #중간부품 adj을 만들기 위해 p가 num개 만큼 필요함
                need_parts[adj][p] += num 
            #중간부품이면
            else:
                for i in range(1,n+1):
                #중간부품 adj를 만들기 위해서는 중간부품p의 부품들이 num개씩 필요한데, 
                #어떤 중간부품들이 필요한지 i로 돌려 하나씩 확인하여 더해줌 
                    need_parts[adj][i] += need_parts[p][i] * num

            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                que.append(adj)

    for i in range(1,n+1):
        if need_parts[n][i] > 0:
            print(i,need_parts[n][i])

for i in range(m):
    mid, base, num = map(int,input().split())

    graph[base].append((mid,num))
    in_degree[mid] += 1

topological_sort()
