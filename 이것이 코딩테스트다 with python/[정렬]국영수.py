<<<<<<< HEAD
N = int(input())

arr = []
for i in range(N):
    data = input().split()
    arr.append(data)

arr = sorted(arr, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )

for i in arr:
    print(i[0])
=======
N = int(input())

arr = []
for i in range(N):
    data = input().split()
    arr.append(data)

arr = sorted(arr, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )

for i in arr:
    print(i[0])
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
