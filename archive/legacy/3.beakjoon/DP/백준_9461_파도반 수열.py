
t = int(input())

arr = [0]*101

arr[0] = 1
arr[1] = 1
arr[2] = 1
arr[3] = 2
arr[4] = 2

for i in range(5,101):
    arr[i] = arr[i-1]+arr[i-5]


for j in range(t):
    k = int(input())
    print(arr[k-1],end=' ')



