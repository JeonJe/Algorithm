
bingo = [list(map(int,input().split())) for _ in range(5)]
seq = [list(map(int,input().split())) for _ in range(5)]


def count_bingo(bingo):
    #가로 빙고 개수 
    cnt = 0
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if bingo[i][j] != -1:
                is_bingo = False
                break
        if is_bingo:
            cnt += 1

    #세로 빙고 개수 
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if bingo[j][i] != -1:
                is_bingo = False
                break 
        if is_bingo:
            cnt += 1
    
    #우측 하단 빙고 개수 
    is_bingo = True
    for i in range(5):
        if bingo[i][i] != -1:
            is_bingo = False
            break
    if is_bingo:
        cnt += 1

    #우측 상단 빙고 개수 
    is_bingo = True
    for i in range(5):
        if bingo[i][4-i] != -1:
            is_bingo = False
            break
    if is_bingo:
        cnt += 1

    return cnt 

def check(bingo, cur):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == cur:
                bingo[i][j] = -1
    
    if count_bingo(bingo) >= 3:
        return True 
    else:
        return False 

answer = 0
for i in range(5):
    for j in range(5):
        cur = seq[i][j]

        if check(bingo, cur):
            print(answer+1)
            exit(0)
            
        answer += 1
