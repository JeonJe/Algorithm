N,S = map(int, input().split())
arr = list(map(int,input().split()))



visited = [False] * (len(arr))
#부분수열 

global temp
global res
global cnt
cnt=0
res = []

def dfs(depth):
    global res
    global cnt

    if depth > N :
        return

    if 1 < depth <= N and sum(temp) == S :
        if temp not in res:
            res.append(temp)
            cnt+=1
        return

  #주어지 순열을 더 확인해야한다면?
    else:
        for i in range(N):
            #다른 인덱스를 방문하지 않았다면?
            if visited[i] == False:
                #방문 표시
                visited[i] = True 
                #방문한 해당 값 넣기
                temp[i] = arr[i]
                
                dfs(depth+1)
                #방문해제
                visited[i] = False
                #값 초기화
                temp[i] = 0
        

temp = [0] * N


dfs(0)
print(cnt)