
n = int(input())


pos = [0] * n

global cnt 
cnt = 0

#같은 행에 배치했는지 체크, True면 해당 열에 배치 됨 
flag_a = [False] * n 
#오른쪽 위 , 왼쪽 아래 방향 대각선으로 퀸을 배치 했는지 체크 
flag_b = [False] * (2*n-1)
flag_c = [False] * (2*n-1) 


def queen(x):
    global cnt
    #y는 몇번쨰 행인지 나타냄 
    for y in range(n):
        #flag_b : 오른쪽 위 , 왼쪽 아래 대각선 확인 - j행 i열의 값은 i+j 
        #flag_c : 왼쪽 위, 오른쪽 아래 대각선 확인 -  j행의 i열의 값은 i - j + (n-1)
        if  not flag_a[y] and not flag_b[x+y] and not flag_c[x - y + (n-1) ]:

            if x == (n-1):
                cnt+=1
            else:
                flag_a[y] = flag_b[x+y] = flag_c[x-y+(n-1)] = True 
                queen(x + 1)
                flag_a[y] = flag_b[x+y] = flag_c[x-y+(n-1)] = False

queen(0)
print(cnt)