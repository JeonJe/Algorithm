N = int(input())

arr = []
for i in range(N):
    data = input().split()
    arr.append(data)

arr = sorted(arr, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )

for i in arr:
    print(i[0])
