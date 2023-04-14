directions = {
    "U" : [1,0],
    "R" : [0,1],
    "D" : [-1,0],
    "L" : [0,-1]
}

def solution(dirs):
    answer = 0
    borad = [[0 for _ in range(11)] for _ in range(11)]
    moves = set()
    x, y = 5,5
    
    for d in dirs:
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if 0 <= nx < 11 and 0 <= ny < 11:
            if (x,y,nx,ny) not in moves and (nx,ny,x,y) not in moves:
                moves.add((x,y, nx,ny))
            x, y = nx, ny
    
    
    return len(moves)
