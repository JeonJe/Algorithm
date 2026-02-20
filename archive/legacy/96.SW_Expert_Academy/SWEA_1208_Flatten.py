T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    seq = list(map(int,input().split()))

    for i in range(n):
        
        top = seq.index(max(seq))
        bottom = seq.index(min(seq))

        seq[top] -= 1
        seq[bottom] += 1

    print(f'#{test_case} {max(seq)-min(seq)}')