import sys
from collections import deque

# sys.stdin = open("input.txt",'rt')  
deq = deque()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(N):
    deq.append((i,arr[i]))


while True:
    cur = deq.popleft()
    index = cur[0]
    risk = cur[1]
    emergency = max(deq, key=lambda x : x[1])[1]

    #처리해야하느 환자
    if risk >= emergency:
        #M번째 환자이면 반복문 탈출
        if index == M:
          break

    else:
        #환자 맨 뒤로
        deq.append((index,risk))

#전체 환자 수 - 남은 환자 수 
print(N-len(deq))


