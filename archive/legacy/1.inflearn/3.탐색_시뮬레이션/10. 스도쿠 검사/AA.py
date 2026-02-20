
import sys
# sys.stdin = open("input.txt",'rt')

res = True

def CheckSdoku (check):
    
    for i in check:        
        if int(i) != 0:
            return False
    return True


arr = [ list(map(int,input().split())) for _ in range(9)]

#왼, 왼위, 위, 오위, 오, 오아, 아, 왼아
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,1,0,1,1,1]

suqaresum = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7),]



for i in range(9):
    col_sum = 0
    row_sum = 0
    col_check = [1]*9
    row_check = [1]*9
    for j in range(9):
        row_check[arr[i][j]-1] -=1
        col_check[arr[j][i]-1] -=1
    
    a = CheckSdoku(col_check)
    b = CheckSdoku(row_check)

    if a and b:
        continue
    else:
        res = False
         

for z in suqaresum:
    sy = z[0]
    sx = z[1]
    check = [1]*9
    
    check[arr[sy][sx]-1]-=1
    for w in range(8):
        ny = sy+dy[w]
        nx = sx+dx[w]

        if ny < 0 or ny>=9 or nx<0 or nx>=9:
            continue
        check[arr[ny][nx]-1]-=1
    c = CheckSdoku(check)

    if c:
        continue
    else:
        res = False
    
    
if res :
    print("YES")
else:
    print("NO")
    

