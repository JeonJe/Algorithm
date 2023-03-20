# 임의의 젊은 날의 행복도는 임의의 늙은 날의 행복도보다 높다.
# 임의의 젊은 날의 피로도는 임의의 늙은 날의 피로도보다 낮다.

import sys 
input = sys.stdin.readline

n = int(input())
day = [ list(map(int,input().split())) for _ in range(n) ]
day.insert(0,[0,0])
young = [ [] for _ in range(n+1) ]
old = [ [] for _ in range(n+1) ]

min_happy, max_happy = sys.maxsize, -sys.maxsize
min_tired, max_tired = sys.maxsize, -sys.maxsize

#젊은날의 최소 행복도와 최대 피로도를 찾음 -> 늙은 날 최대 행복도와 최소 피로도와 비교하기 위해

for i in range(1, n + 1):
    if day[i][0] != 0 and day[i][0] < min_happy:
        min_happy = day[i][0]
    if day[i][1] != 0 and day[i][1] > max_tired:
        max_tired = day[i][1]
    young[i] = [min_happy, max_tired]

for i in range(n, 0, -1):
    if day[i][0] != 0 and day[i][0] > max_happy:
        max_happy = day[i][0]
    if day[i][1] != 0 and day[i][1] < min_tired:
        min_tired = day[i][1]
    old[i] = [max_happy, min_tired]

cnt = -1
for i in range(n - 1, 0, -1):
    young_happy = young[i][0]
    young_tired = young[i][1]
    old_happy = old[i + 1][0]
    old_tired = old[i + 1][1]

    if young_happy > old_happy and young_tired < old_tired and cnt < i:
        cnt = i

print(cnt)