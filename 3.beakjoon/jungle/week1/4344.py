import math 

C = int(input())

for i in range(C):
    arr = list(map(int,input().split()))
    N = arr[0]
    points = arr[1:]
    average = sum(points) // len(points)
    over = [s for s in points if s > average ]
    percent = len(over) / N * 100 
    print( f"{round(percent,3):.3f}%")