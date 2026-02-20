#테스트 케이스 수 
t = int(input())
#나타내야 하는 수


#나타낼 수 있는 방법의 수 
global cnt
cnt = 0

temp = [1,2,3]

def dfs(depth, sum):
    global cnt
    if sum > n:
        return
    elif sum == n:
        cnt+=1
    else:
        for i in range(len(temp)):
            dfs(depth+1,sum+temp[i])

for _ in range(t):
    cnt = 0
    n = int(input())
    dfs(0,0)
    print(cnt)
