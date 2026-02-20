N = 100
area = [[False for i in range(N)] for i in range(N)]

n = int(input())

for i in range(n):
  distance_y, distance_x = map(int,input().split())

  for i in range(distance_x,distance_x+10):
    for j in range(distance_y,distance_y+10):
      area[i][j] = True

cnt_area = 0

for i in range(N):
  for j in range(N):
    if area[i][j]:
      cnt_area += 1

print(cnt_area)
