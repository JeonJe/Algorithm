n = int(input())

points = [ list(map(int,input().split())) for _ in range(n) ]

points.sort(key=lambda x : (x[0], x[1]))

for x,y in points:
    print(x, y)
