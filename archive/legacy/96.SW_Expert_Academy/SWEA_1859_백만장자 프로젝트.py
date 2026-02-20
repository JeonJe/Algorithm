
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    seq = list(map(int,input().split()))

    max_value = -1
    answer =  0
    for i in range(len(seq)-1,-1,-1):
        if seq[i] >= max_value:
            max_value = seq[i]
        else:
            answer += max_value - seq[i]


    print(f'#{test_case} {answer}')
       
