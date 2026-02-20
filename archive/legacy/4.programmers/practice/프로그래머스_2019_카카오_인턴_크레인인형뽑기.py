
def solution(board, moves):
    answer = 0
    len_board = len(boards)
    stack = [ [] for _ in range(len_board)]
    bucket = []
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] != 0:
                stack[j].append(board[i][j])

    for i in range(len_board):
        stack[i].reverse()
    
    for m in moves:
        select = 0
        if stack[m-1]:
            select = stack[m-1].pop()
        if len(bucket) > 0 and select == bucket[-1]:
            answer += 1
            bucket.pop()
        elif select > 0:
            bucket.append(select)

    return answer*2


boards = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

print(solution(boards, moves))