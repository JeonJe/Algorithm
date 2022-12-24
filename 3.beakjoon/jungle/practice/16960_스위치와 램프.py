#스위치 수 N, 램프의 수 M

N, M = map(int,input().split())
graph = [ [] for _ in range(N+1)]
tunon = [0] * (M+1)

for i in range(1,N+1):
    info = list(map(int,input().split()))
    switchs = info[1:]
    for switch in switchs:
        graph[i].append(switch)
        tunon[switch]+=1

# print(graph)       
# print(tunon)
for i in range(1,N+1):
    temp = tunon[:]
    for j in graph[i]:
        temp[j] -= 1
    #스위치 하나만 껏는데도 모든 불이 다 켜있는 경우 == 
    #N-1의 스위치를 눌러서 모든불이 다 켜있는 경우
    if temp[1:].count(0) == 0:
        print(1)
        exit()

print(0)

    
