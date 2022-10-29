T = int(input())

for i in range(T):
    r, arr = map(str, input().split())
    r = int(r)
    for j in range(len(arr)):
        print(arr[j]*r,end='')
    print()
