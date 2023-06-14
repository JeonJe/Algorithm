from collections import defaultdict
import sys 

input = sys.stdin.readline
t = int(input())

def dfs(depth, path):
    global answer, seq, visited
    
    if len(path) >= len(seq):
        print("".join(path))
        return 

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            path.append(k)
            
            dfs(depth+1, path)
            
            path.pop()
            visited[k] += 1

for _ in range(t):
    seq = list(input().strip())
    seq.sort()

    answer = []
    visited = defaultdict(int)

    for chr in seq:
        visited[chr] += 1
        
    
    dfs(0,[])

    
