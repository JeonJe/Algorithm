n, m = map(int,input().split())

points = list(map(int,input().split()))
negative_position = []
positive_position = []

farthest = 0
distnace = 0
for p in points:
    if p >= 0:
        positive_position.append(p)
    else:
        negative_position.append(abs(p))
    farthest = max(farthest, abs(p))

positive_position.sort(reverse=True)
negative_position.sort(reverse=True)

for i in range(0,len(positive_position),m):
    if positive_position[i] == farthest:
        distnace += positive_position[i]
    else:
        distnace += positive_position[i] * 2

for j in range(0,len(negative_position),m):
    if negative_position[j] == farthest:
        distnace += negative_position[j]
    else:
        distnace += negative_position[j] * 2
print(distnace)