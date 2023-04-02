def solution(k, dungeons):
    def dfs(visited,path):
        global answer 
 
        if len(path) >= len(dungeons):
            temp = k
            cnt = 0
            for cur in path:
                need, use = dungeons[cur][0], dungeons[cur][1] 
                if temp >= need and temp >= use:
                    temp -= use
                    cnt+=1
            answer = max(answer,cnt)
            
        for i in range(len(dungeons)):
            if not visited[i]:
                visited[i] = True 
                path.append(i)
                dfs(visited, path)
                path.pop()
                visited[i] = False

    global answer
    answer = 0
    n = len(dungeons)
    visited = [False] * n

    for i in range(n):
        visited = [False for _ in range(n)]
        visited[i] = True
        dfs(visited, [i])

    return answer