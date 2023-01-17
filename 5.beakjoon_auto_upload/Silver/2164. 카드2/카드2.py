from collections import deque

n = int(input())
que = deque()
arr = [ e for e in range(1,n+1)]
que = deque(arr)
# print(arr)

if n == 1:
    print(que[0])
    exit()
    
while len(que) > 1:
    que.popleft()
    if len(que) > 1:
        que.append(que.popleft())
    else:
        print(que[0])
        break
