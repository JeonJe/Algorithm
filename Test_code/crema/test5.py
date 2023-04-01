#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict,deque


def bfs(graph,n,visitNodes):
    visitNodes = set(visitNodes)    
    q = deque([(1,0,set())])

    while q:
        node,path_len,visited = q.popleft()
        visited= visited | {node}
        #모두 방문
        if node == n and visitNodes.issubset(visited):
            return path_len
        #남아있으면 큐에 넣음
        for adj in graph[node]:
            q.append((adj,path_len+1,visited))


def minimumTreePath(n, edges, visitNodes):
    # Write your code here
    graph = defaultdict(list)
    for fr,to in edges:
        graph[fr].append(to)
        graph[to].append(fr)
    return bfs(graph,n,visitNodes)


n = 3
edges = [[1,2],[1,3]]
visitNode = [2]

print(minimumTreePath(n,edges,visitNode))