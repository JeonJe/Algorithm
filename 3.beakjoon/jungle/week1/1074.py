n,r,c = map(int,input().split())

#자르기
global cnt
cnt = 0

#y가 컬럼과 비교되기 때문에 y를 수학적으로 x좌료로 봐야함 
def dfs(x, y, n):
    global cnt
    #[가지치기] r,c가 x,y 로 주어진 사각형에 포함되지 않으면 사각형의 제곱만큼 숫자가 들어갈 수 있기 떄문에 
    # n**2 만큼 cnt 증가 
    if x > r or x+n <= r or y > c or y+n <= c :
        cnt += n ** 2 
        return 
    
    #[정복]
    if n <= 2:
        if x==r and y==c:
            print(cnt)
        elif x==r and y+1==c:
            print(cnt+1)
        elif x+1==r and y==c:
            print(cnt+2)
        else:
            print(cnt+3)
        exit()
    else:
        #[분할] 정사각형 4분할 (Z의 순서이기 때문에 확인하는 순서도 중요, elfi ) 
        ##   x,y     x,y+n   
        ##   x+n,y   x+n,y+n 
        n = n // 2
        dfs (x, y, n)
        dfs (x, y+n, n)
        dfs (x+n, y, n)
        dfs (x+n, y+n, n)


cnt = 0

#2**은 사각형의 한 변의 길이 
dfs(0,0,2**n)


