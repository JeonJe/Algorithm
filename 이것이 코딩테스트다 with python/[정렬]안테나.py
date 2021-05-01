N = int(input())

data = list(map(int,input().split()))

data = sorted(data)
print(data[(N-1)//2])

