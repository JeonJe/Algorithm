N = int(input())

arr =[]
for _ in range(N):
    arr.append(int(input()))

arr.sort()
arr.reverse()
#sorted(arr,reverse=True)
for i in arr:
    print(i)