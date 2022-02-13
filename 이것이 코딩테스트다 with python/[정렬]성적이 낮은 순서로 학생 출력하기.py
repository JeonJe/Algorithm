N = int(input())

arr = []


for _ in range(N):
    Name,Score = input().split()
    arr.append((Name,Score))

print(arr)

result = sorted(arr,key=lambda Score : Score)

for i in result:
    print(i[0])