t = int(input())
for test_case in range(1,t+1):
    m = int(input())
    graph = [ list(input()) for _ in range(m) ]
    answer = 0
    if m == 1:
        answer = int(graph[0][0])
    else:
        mid = m // 2
        left,right = mid, mid + 1

        for i in range(m//2):
            answer += sum(list(map(int,graph[i][left:right])))
            left -= 1
            right += 1

        answer += sum(list(map(int,graph[mid])))

        for i in range(m//2+1,m):
            left += 1
            right -= 1
            answer += sum(list(map(int,graph[i][left:right])))
            
    print(f'#{test_case} {answer}')