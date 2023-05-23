import sys 
input = sys.stdin.readline 

T = 1

for test_case in range(1, T + 1):
    n = int(input())
    seq = list(map(int,input().split()))
    answer = 0
    for i in range(2,n-2):
        side_view = max(seq[i-2],seq[i-1],seq[i+1],seq[i+2])
        if side_view >= seq[i]:
            continue
        else:
            answer += seq[i] - side_view

    print(f'#{test_case} {answer}')
       
