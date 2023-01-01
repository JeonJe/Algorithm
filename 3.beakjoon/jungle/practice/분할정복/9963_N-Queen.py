import sys 


N = int(input())

row = [-1] *(N)
global cnt 
cnt = 0

# x는 몇 번 쨰 row인지

def is_valid_place(x):
    #이전 row들만 봐서 확인
    for i in range(x):
           #열이 같으면 안됨            대각선도 같아선 안됨
        if row[i] == row[x] or (abs(x-i) == abs(row[x]-row[i])):
            return False
    return True


def nqueen(depth):
    global cnt 
    #모든 row에 queen을 하나씩 놓을 수 있으면 경우의의 수 추가 
    if depth == N:
        cnt += 1
        return 

    for i in range(N):
        row[depth] = i
        if is_valid_place(depth):
            nqueen(depth+1)

                
nqueen(0)

print(cnt)