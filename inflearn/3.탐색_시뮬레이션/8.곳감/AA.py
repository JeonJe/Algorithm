
import sys
# sys.stdin = open("input.txt",'rt')


def printarr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
        print

def rot(arr, rnum,direction,rotnum):

    rotnum %= len(arr)

    if direction == 0:
        for _ in range(rotnum):
            arr[rnum-1].append(arr[rnum-1].pop(0))
        
        
        
    else:
        for _ in range(rotnum):
            arr[rnum-1].insert(0,arr[rnum-1].pop())

    return arr 

N = int(input())
arr = []

#arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(N):
    arr.append( list(map(int,input().split())))

M = int(input())
for i in range(M):
    rnum, direction, rotnum = map(int,input().split())
    # 회전 정보에 따라 돌림
    
    arr = rot(arr, rnum,direction,rotnum)


#곶감모양판 덧셈
left,right = 0, N
mid = N // 2

total = 0
for i in range(N):
    for j in range(left,right):
        total+= arr[i][j]

    if i < mid:
        left+=1
        right-=1

    else:
        left-=1
        right+=1

print(total)