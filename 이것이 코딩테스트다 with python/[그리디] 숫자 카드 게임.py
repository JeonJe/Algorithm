N,M = map(int,input().split())

result = -1
for _ in range(N):
    data = (list(map(int,input().split()))) # 한 행 읽기
    min_value = min(data) # 한 행에서 가장 작은 수 찾기
    result = max(result,min_value) #읽어드린 행의 가장 작은 수중 가장 큰 수 찾기 

print(result)