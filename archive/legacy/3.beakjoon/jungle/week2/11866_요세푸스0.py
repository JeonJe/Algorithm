
# from collections import deque

# N, K = map(int,input().split())

# que = deque()
# for i in range(N):
#     que.append(i+1)
# res = []
# idx = 1

# while len(que) > 1:
#     x = que.popleft()
#     if idx % K != 0:
#         que.append(x)
#     else:
#         res.append(x)
#         idx = 0
#     idx += 1

# res.append(que[0])
# r = ", ".join(map(str,res))
# print(f'<{r}>')

N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
idx = 0
yose = []
while len(arr) != 0:
    idx = (idx + K - 1) % len(arr)
    yose.append(arr[idx])
    arr.remove(arr[idx])
    
yose = map(str, yose)
print(f"<{', '.join(yose)}>")