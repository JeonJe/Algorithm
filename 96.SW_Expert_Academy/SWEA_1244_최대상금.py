
def dfs(num, cnt):
    global answer
    if cnt == change_cnt:
        answer = max(answer, int("".join(num)))
        return 

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            temp = int("".join(num))
            if (temp,cnt) not in visited:
                visited.append((temp,cnt))
                dfs(num, cnt+1)
            num[i],num[j] = num[j],num[i]
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num, change_cnt = map(int,input().split())
    num = list(str(num))
    global answer 
    answer = 0
    visited = []
    dfs(num,0)

    print(f'#{test_case} {answer}')


    