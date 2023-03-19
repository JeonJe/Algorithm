from itertools import permutations

n  = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
perm = list(permutations(arr, 3))

answer = 0
for c in perm:
    x1,y1 = c[0][0],c[0][1]
    x2,y2 = c[1][0],c[1][1]
    x3,y3 = c[2][0],c[2][1]
    if x1 != x2 or y1 != y2:
        continue

    if (x1-x2)**2 + (y1-y2)**2 + (x2-x3)**2 + (y2-y3)**2 == (x1-x3)**2 + (y1-y3)**2:
        answer += 1
print(answer)