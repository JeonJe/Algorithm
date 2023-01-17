# 회사에서 각 영업 사원의 실적을 관리하고 있습니다. 매월 실적에 따라 성과급을 지급하고 있
# 습니다. 성과급을 지급하는 조건은 다음과 같습니다.
# 1. 당월 실적이 70점 이상이면서 실적 순위가 상위 20% 이내인 사원
# 2. 당월 실적이 70점 이상이면서 1등인 사원
# 3. 전월 실적과 비교하여 당월 실적이 가장 많이 오른 사원(중복 허용)
# 단, 동점인 경우 실적 순위는 같으며, 중복으로 성과급을 받을 수 없습니다.
# 성과급 지급 대상 사원이 몇 명인지 구하기 위해 다음과 같이 프로그램 구조를 작성했습니다.
# 1. 당월 실적을 기준으로 사원들의 실적 순위를 구합니다.
# 2. 각 사원별로 (당월 실적 – 전월 실적) 중 최댓값을 구합니다.
# 3. 아래 조건을 만족하는 사원을 발견하면, 성과급 지급 대상자 수를 1 증가시킵
# 니다.
# 3-1. 당월 실적이 70점 이상이고, 실적 순위가 상위 20% 이내인 경우
# 3-2. 또는 당월 실적이 70점 이상이고, 실적 순위가 1등인 경우
# 3-3. 또는 (당월 실적 – 전월 실적)이 2단계에서 구한 값과 같고, 그 값이 양
# 수인 경우
# 4. 성과급 지급 대상자 수를 return 합니다.
# 사원들의 당월 실적을 담고 있는 리스트 cur_month, 전월 실적을 담고 있는 리스트
# pre_month가 매개변수로 주어질 때 성과급 지급 대상자 수를 return 하도록 solution 함수를
# 작성하려고 합니다. 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진
# func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

def func_a(cur_sale, pre_sale, rank, max_up): #3번
    sale_len = len(cur_sale)
    count = 0
    for i in range(sale_len):
        if cur_sale[i] >= 70 and rank[i] <= sale_len // 5:
            count += 1
        elif cur_sale[i] >= 70 and rank[i] == 1:
            count += 1
        elif max_up > 0 and max_up == cur_sale[i] - pre_sale[i]:
            count += 1
    return count

def func_b(cur_sale, pre_sale):  # 2번
    max_up = 0
    for i in range(len(cur_sale)):
        max_up = max(max_up, cur_sale[i] - pre_sale[i])
    return max_up

def func_c(cur_sale):
    sale_len = len(cur_sale)
    rank = [1] * sale_len
    for i in range(sale_len):
        for j in range(sale_len):
            if cur_sale[i] < cur_sale[j]:
                rank[i] += 1
    return rank

def solution(cur_sale, pre_sale):
    rank = func_c(cur_sale)
    max_up = func_b(cur_sale, pre_sale)
    answer = func_a(cur_sale, pre_sale, rank, max_up)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cur_month = [20, 50, 35, 80, 75]
pre_month = [15, 55, 75, 85, 75]
ret = solution(cur_month, pre_month)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
