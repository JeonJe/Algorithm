n = int(input())
arr = list(map(int,input().split()))

max_point = max(arr)

s = 0 
for i in range(len(arr)):
    arr[i] = arr[i]/max_point*100
    s+= arr[i]

print(s/n)

