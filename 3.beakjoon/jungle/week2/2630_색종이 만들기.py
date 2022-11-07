n = int(input())

imap = [ list(map(int,input().split())) for _ in range(n) ]

global white
global blue 
white = 0
blue = 0

def dfs (x,y,n):
    global white
    global blue
    temp_sum = 0
    # 1개이면 분할 더 이상 못함
    if n == 1:
        if imap[x][y] == 1:
            blue += 1
        elif imap[x][y] == 0:
            white += 1
        return
    #분할 해야하는지 확인 
    if n >= 2:
        for i in range(x,x+n):
            for j in range(y,y+n):
                temp_sum +=  imap[i][j]
        if temp_sum == 0:
            white+=1
            return
        elif temp_sum == n ** 2:
            blue+=1
            return 
        else:
            n = n //2
            dfs(x, y, n)
            dfs(x+n, y, n)
            dfs(x, y+n, n)
            dfs(x+n, y+n, n)

dfs(0,0,n)
print(white)
print(blue)