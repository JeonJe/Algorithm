n = int(input())

arr = [ list(map(int,input())) for _ in range(n)]

def dfs(x,y,n):

    if n == 1:
        print(arr[x][y],end='')
        return
    
    if n>=2:
        s = 0
        #가지치기 
        for i in range(x, x+n):
            for j in range(y, y+n):
                s+=arr[i][j]
        if s == 0:
            print('0',end='')
        elif s == 1*(n**2):
            print('1',end='')
        else:
            print('(',end='')
            n = n // 2
            dfs(x,y,n)
            dfs(x,y+n,n)
            dfs(x+n,y,n)
            dfs(x+n,y+n,n)
            print(')',end='')

dfs(0,0,n)