
def solution(rows, columns, queries):
    answer = []
    graph = [[0] * columns for _ in range(rows)]
    
    v = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = v
            v+=1
    
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1

        rt = graph[x1][y2]
        min_value = rt

        #left to right
        for i in range(y2,y1,-1):
            graph[x1][i] = graph[x1][i-1]
            min_value = min(min_value, graph[x1][i])

        #bottom to top
        for i in range(x1,x2):
            graph[i][y1] = graph[i+1][y1]
            min_value = min(min_value, graph[i][y1])
        
        #right to left
        for i in range(y1,y2):
            graph[x2][i] = graph[x2][i+1]
            min_value = min(min_value, graph[x2][i])
        
        #bottom to top
        for i in range(x2,x1,-1):
            graph[i][y2] = graph[i-1][y2]
            min_value = min(min_value, graph[i][y2])
        
        graph[x1+1][y2] = rt
        answer.append(min_value)
    
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns,queries))


