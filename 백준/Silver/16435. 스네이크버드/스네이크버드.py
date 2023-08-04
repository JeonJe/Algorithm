n, current = map(int,input().split())

heights = list(map(int,input().split()))
heights.sort()

for i in range(len(heights)):
    if heights[i] <= current:
        current += 1
print(current) 