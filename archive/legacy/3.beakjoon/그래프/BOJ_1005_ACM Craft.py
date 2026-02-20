from collections import deque, defaultdict
import sys
input = sys.stdin.readline

t = int(input())

def topological_sort():
    total_time = defaultdict(int)

    while que:
        current  = que.popleft()
        if current == destination:
            return total_time[current] + times[current-1]

        for adj in graph[current]:
            in_degree[adj] -= 1
            total_time[adj] = max(total_time[adj], total_time[current]+ times[current-1])

            if in_degree[adj] == 0:
                que.append((adj))


for _ in range(t):
    num_of_building, rules = map(int,input().split())
    times = list(map(int,input().split()))
    seq = [list(map(int,input().split()))for _ in range(rules)]
    destination = int(input())
    
    in_degree = [0]*(num_of_building+1)

    graph = [ [] for _ in range(num_of_building+1)]
    for fr, to in seq:
        graph[fr].append(to)
        in_degree[to] += 1

    que = deque()
    for i in range(1,len(in_degree)):
        if in_degree[i] == 0:
            que.append(i)
    
    print(topological_sort())




