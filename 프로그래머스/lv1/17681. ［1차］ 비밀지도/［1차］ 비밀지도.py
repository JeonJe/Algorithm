def solution(n, arr1, arr2):
    answer = []
    #arr1을 graph로 그리기 
    graph_arr1 = [[] for _ in range(n)]
    graph_arr2 = [[] for _ in range(n)]
    graph = [[" "]*n for _ in range(n)]
    
    for i in range(len(arr1)):
        row = list(bin(arr1[i])[2:].zfill(n))
        for r in row:
            graph_arr1[i].append(r)
        
    for i in range(len(arr2)):
        row = list(bin(arr2[i])[2:].zfill(n))
        for r in row:
            graph_arr2[i].append(r)
            
    for i in range(n):
        for j in range(n):
            if graph_arr1[i][j] == '1' or  graph_arr2[i][j] == '1':
                graph[i][j] = '#'
    res = []        
    for g in graph:
        res.append(''.join(g))
    return res
                
            
    
    
    
    return answer