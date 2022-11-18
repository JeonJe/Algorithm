from collections import deque

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1) ]
in_degree = [0]*(n+1)

def topological_sort():
    need_parts =[ [0]*(n+1) for _ in range(n+1) ]
    que = deque()

    for i in range(1,n+1):
        if in_degree[i] == 0:
            que.append(i)
         

    while que:
        now_node = que.popleft()
        # now_node는 next_node를 만들기 위해 num만큼의 개수가 필요 
        for next_node,num in graph[now_node]:
            #기본부품
            #중간부품을 만들기 위해 필요한 now_node가 기본제품이면

            if need_parts[now_node].count(0) == n+1:
                #중간부품 next_node을 만들기 위해 now_node가 num개 만큼 필요함
                need_parts[next_node][now_node] += num 
            #중간부품이면
            else:
                for i in range(1,n+1):
                #중간부품 next_node를 만들기 위해서는 중간부품 now_node의 부품들이 num개씩 필요한데, 
                #now_node를 위한 부품들을 i로 돌려 하나씩 확인하여 num 개수만큼 곱해서 더해줌 
                    need_parts[next_node][i] += need_parts[now_node][i] * num

            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                que.append(next_node)

    for i in range(1,n+1):
        if need_parts[n][i] > 0:
            print(i,need_parts[n][i])

for i in range(m):
    mid, base, num = map(int,input().split())

    graph[base].append((mid,num))
    in_degree[mid] += 1

topological_sort()
