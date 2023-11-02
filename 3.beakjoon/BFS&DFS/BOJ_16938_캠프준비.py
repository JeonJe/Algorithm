N, L, R, X = map(int,input().split())
problems = list(map(int,input().split()))

def check(case):
    min_diff = 10**6
    max_diff = 1
    cnt, sum_diff = 0, 0 

    # case로 표현된 문제 선택조합에서 선택된 문제 수 최대 문제 난이도, 최소 문제 난이도, 난이도 합을 구함
    for i in range(N):
        flag = case & ( 1 << i )

        #i번쨰 문제가 선택 된 경우 
        if flag:
            min_diff = min(min_diff, problems[i]) 
            max_diff = max(max_diff, problems[i])        
            sum_diff += problems[i]
            cnt += 1
    
    if L <= sum_diff <= R and cnt >= 2 and max_diff - min_diff >= X:
        return True
    return False 

answer = 0
for case in range(2**N):
    if check(case):
        answer += 1
print(answer)