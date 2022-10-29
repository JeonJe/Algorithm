
import sys
from collections import deque
sys.stdin = open("input.txt",'rt')

dy = [1,2,2,1,-1,-2,-2,-1]
dx = [-2,-1,1,2,2,1,-1,-2]


def BFS(cy,cx,fy,fx):

    Map[cy][cx] = 1
    hop[cy][cx] = 0

    deq = deque()
    deq.append((cy,cx))

    while deq:
        y,x = deq.popleft()
        
        if y==fy and x==fx:
            print(hop[y][x]) 
            return

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=nx<I and 0<=ny<I and Map[ny][nx]==0 :
                Map[ny][nx]=1
                hop[ny][nx]= hop[y][x]+1
                deq.append((ny,nx))

if __name__ == "__main__":
    T = int(input()) #테스트 케이스 개수 
    for _ in range(T):
        
        I = int(input()) # 체스판 한변의 길이 
        current_y,current_x = map(int,input().split())
        final_y,final_x = map(int,input().split())
    
        Map = [ [0 for _ in range(I)] for _ in range(I)]
        hop=[ [0 for _ in range(I)] for _ in range(I)]
        
    
        BFS(current_y,current_x,final_y,final_x)
  