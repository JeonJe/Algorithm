n = int(input())
student = [list(map(int,input().split())) for _ in range(n**2)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = [[0 for _ in range(n)] for _ in range(n)]
total_satisfied = 0

def set_positions():
    
    global total_satisfied
    for s in range(len(student)):
      k = student[s][0]
      
      # (좋아하는 학생 수, 빈칸 수, 행번호, 열번호)
      # 정렬기준은 0번 내림차순, 1번 내림차순, 2번 오름차순, 3번 오름차순
      position_candidates =[]
      for i in range(n):
          for j in range(n):
              cnt_like, cnt_empty = 0, 0
              if board[i][j] == 0:
                  for direction in range(4):
                      nx = i + dx[direction]
                      ny = j + dy[direction]

                      if 0 <= nx < n and 0 <= ny < n:
                          if board[nx][ny] == 0:
                              cnt_empty += 1
                          elif board[nx][ny] in student[s][1:]:
                              cnt_like += 1
                  position_candidates.append([cnt_like,cnt_empty,i,j])
      
      position_candidates.sort(key=lambda x : (-x[0],-x[1],x[2],x[3]))
      best_x, best_y = position_candidates[0][2], position_candidates[0][3]
      board[best_x][best_y] = k
    
def cal_satisfied():
    global total_satisfied
    for s in range(len(student)):
      k = student[s][0]
      for i in range(n):
          for j in range(n):
              cnt_like = 0
              if board[i][j] == k:
                
                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]

                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in student[s][1:]:
                            cnt_like += 1
                total_satisfied += 0 if cnt_like == 0 else 10**(cnt_like - 1)

set_positions()
cal_satisfied()
# print(board)
print(total_satisfied)
