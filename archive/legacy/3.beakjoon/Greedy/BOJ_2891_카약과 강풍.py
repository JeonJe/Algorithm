from collections import deque

N, S, R = map(int,input().split())

broken = list(map(int,input().split()))
extra = list(map(int,input().split()))

for i in range(1,N+1):
    if i in extra and i in broken:
        broken.remove(i)
        extra.remove(i)

for i in range(1,N+1):
    if i in extra:
        if i-1 in broken:
            broken.remove(i-1)
        elif i+1 in broken:
            broken.remove(i+1)

print(len(broken))

    