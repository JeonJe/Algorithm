import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = [ [] for _ in range(n+1) ]
node = [ [], [0,0]]


def dfs( v ):
    #v는 현재 노드
    result = 0 
    
    #현재노드에게 연결된 자식노드들을 dfs로 확인
    for i in graph[v]:
        result += dfs(i)
    
    #현재노드가 양이라면 숫자를 더해준다
    if node[v][0] == 'S':
        result += node[v][1]
    #현재노드가 늑대라면 숫자를 빼준다.
    else:
        result -= node[v][1]
        result = max(0,result)
    
    return result
  
for i in range(1,n):
    t,a,p = input().split()
    #목적지로 연결되는 점들을 append 함 
    graph[int(p)].append(i+1)
    #2.. N번까지 노드의 type과 마릿수를 입력
    node.append([t,int(a)])

print(dfs(1))