import sys 
sys.setrecursionlimit(10**9)

def solution(phone):
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]

    def dfs(x,y, depth,visited,path):
        global answer
        
        if depth >= 12 or not any(visited):
            answer += len(path)
            return
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < height and 0 <= ny < width:
                #다음 점이 가본적없었던 점이면서 인식가능한 점이면 방문
                if not visited[nx][ny] and phone[nx][ny] == 1:
                    visited[nx][ny] = True
                    path.append([nx,ny])
                    answer += 1
                    dfs(nx,ny,depth+1,visited, path)
                    #다른 루트로 방문 시 사용할 수 있도록 방문 표시 해제 
                    visited[nx][ny] = False
                    path.pop()

        return 

    global answer
    answer = 0
    height = 4
    width = 3
    visited = [ [False]*width for _ in range(height) ]

    for i in range(height):
        for j in range(width):
            if phone[i][j] == 1:
                visited[i][j] = True

                #i,j 부터 갈 수 있는 경우의 수를 다 확인해서 answer에 넣기 
                dfs(i,j,0,visited,[])
                visited[i][j] = False

    return answer