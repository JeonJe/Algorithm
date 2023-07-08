
n = int(input())
drinks = list(map(int,input().split()))

drinks.sort()

res = 0
for i in range(n-1):
    res += drinks[i] / 2

res += drinks[-1]

print(res)
