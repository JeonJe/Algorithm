from collections import deque 

N = int(input())
des = [0] * (N+1)
que = deque()

if N == 0:
    print(0)
    exit()

cnt = 0
res = []

for i in range(10):
    que.append((str(i)))
    res.append(i)
    cnt += 1 

if N <= 10:
    print(N)
    exit()

while que:
    c_val = que.popleft()

    for j in range(10):
        if int(c_val[-1]) > j:
            que.append((c_val+str(j)))
            res.append(int(c_val+str(j)))
            if cnt == N:
                print(res[-1])
                exit()
            cnt+=1

print(-1)
