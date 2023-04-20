from collections import deque 
n,k = map(int,input().split())

arr = [i for i in range(1,n+1)] 
deq = deque(arr)
answer = []

while deq:
    for i in range(k-1):
        deq.append(deq.popleft())
    answer.append(str(deq.popleft()))

answer = ", ".join(answer)
print(f'<{answer}>')