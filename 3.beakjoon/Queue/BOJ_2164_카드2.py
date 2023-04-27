from collections import deque 
n = int(input())

seq = [i for i in range(1,n+1)]
que = deque(seq)

while len(que)>1:
    que.popleft()
    que.append(que.popleft())
print(que[0])