<<<<<<< HEAD
N = int(input())

arr = []


for _ in range(N):
    Name,Score = input().split()
    arr.append((Name,Score))

print(arr)

result = sorted(arr,key=lambda Score : Score)

for i in result:
=======
N = int(input())

arr = []


for _ in range(N):
    Name,Score = input().split()
    arr.append((Name,Score))

print(arr)

result = sorted(arr,key=lambda Score : Score)

for i in result:
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
    print(i[0])