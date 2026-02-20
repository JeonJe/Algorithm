n = int(input())
answer = 0
data = [ int(input()) for _ in range(n)]
prev = data[-1]
for i in range(len(data)-2,-1,-1):
    if data[i] >= prev:
        decre = data[i] - prev + 1
        answer += decre
        data[i] -= decre
    prev = data[i]

print(answer)