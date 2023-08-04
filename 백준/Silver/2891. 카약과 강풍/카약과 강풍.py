from collections import deque

N, S, R = map(int,input().split())

broken = list(map(int,input().split()))
extra = list(map(int,input().split()))

temp = []
#여분의 카누를 못 빌려주고 자기가 사용해야 하는 팀
for e in extra:
    if e in broken:
        temp.append(e)

for t in temp:
    extra.remove(t)
    broken.remove(t)

extra_que = deque(extra)
broken_que = deque(broken)

while extra_que:
    cur = extra_que.popleft()
    temp = []
    while broken_que:
        target = broken_que.popleft()
        if abs(target - cur) == 1:
            while broken_que:
                temp.append(broken_que.popleft())
            break
        else:
            temp.append(target)
    broken_que = deque(temp)
        
print(len(broken_que))
