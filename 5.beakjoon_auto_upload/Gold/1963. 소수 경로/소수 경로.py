from collections import deque


def eratos():
    primes[0],primes[1] = False, False
    for i in range(2, int(10000**(1/2))+1 ):
        for j in range(2*i, len(primes), i):
            primes[j] = False

def bfs(s,d):
    que = deque()
    que.append((s,0))    
    visited = [False] * (10000)
    visited[s] = True

    while que:
        cur_num, cur_cnt = que.popleft()
        if cur_num == d:
            return cur_cnt
        #자리 수 이동
        for i in range(4):
            #자리 수 고정 후 값 변경
            for j in range(10): 
                temp = int(str(cur_num)[:i] + str(j) + str(cur_num)[i+1:])
                if temp <= 1000:
                    continue
                if not visited[temp] and primes[temp]:
                    visited[temp] = True
                    que.append((temp, cur_cnt + 1))
    return -1
    

t = int(input())
primes = [True]*(10000)
eratos()

for i in range(t):
    s, d = map(int,input().split())
    res = bfs(s,d)
    print( res if res >= 0 else "Impossible")

