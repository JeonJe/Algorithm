N = int(input())

data = list(map(int,input().split()))

#최솟값을 증가하면서 확인하느냐


data.sort()

target = 1

for x in data:
    print(target, x )
    if target < x:
        break
    target+=x

print(target)