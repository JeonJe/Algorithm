import sys
from collections import deque

# sys.stdin = open("input.txt",'rt')  

deq = deque()

N,K = map(int,input().split())
cnt = 0
cur = 0

for i in range(N):
    deq.append(i+1)

#1명이 남을 때까지 반복
while len(deq)>1:
    #cnt가 K가 될 때까지 반복
    cnt = 1
    while cnt < K:
        cnt+=1
        cur+=1
        cur %= len(deq)
        
    #cnt 가 K와 같아지면 cur인덱스의 왕자 아웃
    deq.remove(deq[cur])
    
 
print(deq[0])



