n,k = map(int,input().split())

arr = [i for i in range(1,n+1)] 
visit = [False for _ in range(n)]
print(arr,visit)
answer = []

point = 0
cur = 0
while not all(visit):    
    #아직 방문하지 않은 애들 확인 
    j = 0
    cur = cur % len(arr)
    while j < k:
        if not visit[cur]:
            j+=1
        else:
            cur+=1
    visit[j-1] = True
    answer.append(arr[j-1])
    
    
print(answer)