n = int(input())

arr = [ int(input()) for _ in range(n)]
arr.sort(reverse=True)
rope_weight = []

for i in range(n):
    rope_weight.append(arr[i]*(i+1))

print(max(rope_weight))

