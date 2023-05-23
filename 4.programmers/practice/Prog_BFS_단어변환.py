from collections import defaultdict,deque

def diff(a,b):
    a,b = list(a), list(b)
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt+=1
    return cnt
            
def make_graph(graph):
        
    for key,_ in graph.items():
        for key2, _ in graph.items():
            if key == key2:
                continue

            if diff(key,key2) == 1:
                graph[key].add(key2)
                graph[key2].add(key)
    
    return 
        
def bfs(graph,begin,target):
    
    que = deque()
    que.append((begin,0))
    visited = defaultdict(bool)
    visited[begin] = True 
    
    while que:
        cur,dist = que.popleft()
        if cur == target:
            return dist
            
        for adj in graph[cur]:

            if not visited[adj]:
                visited[adj] = True
                que.append((adj,dist+1))

    return 0


def solution(begin, target, words):
    
    if target not in words:
        return 0 
    
    graph = defaultdict(set)
    for word in words:
       graph[word] = set()
    graph[begin] = set()

    make_graph(graph)
    for k,v in graph.items():
        print(k,v)
    return bfs(graph,begin,target)

begin = "hit"
target = "cog"
words =["cog","lot","hot", "dot", "dog", "log"]
# words =["hot","dot","dog","lot","log","cog"]
# words =  ["abb", "aba"]

print(solution(begin,target,words))

