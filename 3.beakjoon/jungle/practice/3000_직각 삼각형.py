import itertools

n = int(input())

points = [list(map(int,input().split())) for _ in range(n)]

nCr = list(itertools.combinations(points,3))

for C in nCr:
    x1,y1 = C[0][0], C[0][1]
    x2,y2 = C[1][0], C[1][1]
    x3,y3 = C[2][0], C[2][1]
    
    
    if 
