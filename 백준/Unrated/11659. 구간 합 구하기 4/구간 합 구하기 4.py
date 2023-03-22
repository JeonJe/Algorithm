import sys 
input = sys.stdin.readline
N,M = map(int,input().split())

arr = list(map(int,input().split()))

acc = [0]*(N)
acc[0] = arr[0]
for i in range(1,N):
    acc[i] = arr[i] + acc[i-1]
acc.insert(0,0)

for _ in range(M):
    fr, to = map(int,input().split())
    print(acc[to]-acc[fr-1])
