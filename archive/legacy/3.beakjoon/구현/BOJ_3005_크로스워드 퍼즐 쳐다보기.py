from collections import deque 
R,C = map(int,input().split())

board = [list(input()) for _ in range(R)]
bucket = set()

def find_word(x,y,bucket):
    
    que = deque()
    # 현재 위치에서 좌우로 포인터를 이동시키면서 가로 단어 찾기 
    que.append(board[x][y])
    ly = y - 1
    while 0 <= ly  and board[x][ly] != '#':
        que.appendleft(board[x][ly])
        ly -= 1
    
    ry = y + 1
    while ry < C and board[x][ry] != '#':
        que.append(board[x][ry])
        ry += 1
    
    word = "".join(que)
    if len(word) > 1:
      bucket.add(word)

    que = deque()
    que.append(board[x][y])
    # #현재 위치에서 상하로 포인터를 이동시키면서 세로 단어 찾기 
    tx = x - 1
    while 0 <= tx  and board[tx][y] != '#':
        que.appendleft(board[tx][y])
        tx -= 1
    
    bx = x + 1
    while bx < R and board[bx][y] != '#':
        que.append(board[bx][y])
        bx += 1
  
    word = "".join(que)
    if len(word) > 1:
      bucket.add(word)



for i in range(R):
    for j in range(C):
        if board[i][j] != '#':
          find_word(i,j,bucket)

sorted_bucket = sorted(list(bucket))
print(sorted_bucket[0])
