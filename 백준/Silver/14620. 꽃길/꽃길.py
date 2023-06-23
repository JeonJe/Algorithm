

n = int(input())
board = [ list(map(int,input().split())) for _ in range(n) ]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def find_min_value(coordinates):
    visited = [ [False for _ in range(n)] for _ in range(n) ]

    value = 0
    for x,y in coordinates:
        visited[x][y] = True
        value += board[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]        

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    value += board[nx][ny]
                    visited[nx][ny] = True
                else:
                    return -1
            else:
                return -1
    
    return value


def find_combinations(board, coordinates, depth):
    if depth == 3:
        result = find_min_value(coordinates)
        if result != -1:
            global answer
            answer = min(answer, result)
        return
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) not in coordinates:

                find_combinations(board, coordinates + [(i,j)], depth+1)
        
answer = 1e9
find_combinations(board, [], 0)
print(answer)