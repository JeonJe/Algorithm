t = int(input())

for test_case in range(1,t+1):

    n = list(map(int,input()))
    
    prev = 0
    answer = 0
    for i in range(len(n)):
        if prev != n[i]:
            answer += 1
            prev = n[i]
    
    print(f'#{test_case} {answer}')