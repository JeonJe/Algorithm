def solution(k, dungeons):
    def dfs( visited,path):
        global answer 
 
        if len(path) >= len(dungeons):
            temp = k
            cnt = 0
            for cur in path:
                if temp >= dungeons[cur][0] and temp >= dungeons[cur][1]:
                    temp -= dungeons[cur][1]
                    cnt+=1
            answer = max(answer,cnt)
            
        
        for i in range(len(dungeons)):
            if not visited[i]:
                visited[i] = True 
                path.append(i)
                dfs( visited,  path)
                path.pop()
                visited[i] = False

    global answer
    answer = 0

    visited = [False] * len(dungeons)
    for i in range(len(dungeons)):
        visited = [False for _ in range(len(visited))]
        visited[i] = True
        dfs(visited, [i])

    return answer