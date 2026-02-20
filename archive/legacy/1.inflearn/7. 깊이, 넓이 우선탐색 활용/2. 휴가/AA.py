import sys

# sys.stdin = open("input.txt",'r') 

def dfs(day, sum_money):
    global res
    
    if day > N+1:
        return 
    
    if sum_money > res:
        res = sum_money
    
    if day == N+1:
        return
            
    #day에 상담을 시작하는 경우  
    dfs(day+T[day],sum_money+P[day])
    
    #day에 상담을 시작하지 않는 경우 ->다음일로 넘어감
    dfs(day+1,sum_money)
T=[]
P=[]
N = int(input())
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

T.insert(0,0)
P.insert(0,0)

res = -sys.maxsize -1
dfs(1,0)

print(res)