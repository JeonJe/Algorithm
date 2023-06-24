from collections import defaultdict,deque

#사람수, 파티수
N, M = map(int,input().split())
already_know_info = input()

if already_know_info[0] != "0":
    already_know_persion = list(map(int,already_know_info.split()))[1:]
else:
    already_know_persion = None

graph = [ [] for _ in range(N+1)]
partys = []
for i in range(M):
    data = list(map(int,input().split()))
    people = data[1:]
    partys.append(people)

    #참석자 연결관계 그래프 
    for i in range(len(people)-1):
        for j in range(i+1,len(people)):    
            graph[people[i]].append(people[j])
            graph[people[j]].append(people[i])
cnt = 0

if already_know_persion is None:
    print(M)
    exit(0)
    
for i in range(len(partys)):
    visited = [ False for i in range(N+1) ]
    que = deque()

    if partys[i][0] not in already_know_persion:
        que.append(partys[i][0])
        visited[partys[i][0]] = True
    else:
        continue
    
    is_ok = True

    while que:
        current = que.pop()

        for adj in graph[current]:
            if adj in already_know_persion:
                is_ok = False
                break
            if not visited[adj]:
                visited[adj] = True
                que.append(adj)

    if is_ok:
        cnt += 1
    
print(cnt)
