global r,c,cnt
N, r, c = map(int,input().split())

def dfs(x,y,n):
    global r,c,cnt
    #가지치기 
    # x,y가 범위내에 없으면 return 
    if r < x or r >= x+n or c < y or c >= y+n:
        cnt += n ** 2
        return 


    #분할
    if n >= 2 :
        n = n // 2
        #1사분면
        dfs(x, y ,n)
        #2사분면
        dfs(x, y+n, n)
        #3사분면
        dfs(x+n, y, n)
        #4사분면
        dfs(x+n, y+n, n)

        
    #정복 (쪼갤 수 없을 때)
    else:
        if x==r and y==c:
            print(cnt)
        elif x==r and y+1==c:
            print(cnt+1)
        elif x+1==r and y==c:
            print(cnt+2)
        else:
            print(cnt+3)
        exit() 

cnt = 0
dfs(0,0, 2**(N))