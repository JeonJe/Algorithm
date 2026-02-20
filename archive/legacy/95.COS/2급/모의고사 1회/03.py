# 시작 날짜와 끝 날짜가 주어질 때, 두 날짜가 며칠만큼 떨어져 있는지(D-day)를 구하려 합니다. 이를 위해 다음과 같이 3단
# 계로 간단히 프로그램 구조를 작성했습니다. (단, 윤년은 고려하지 않습니다.)
# 1단계. 시작 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
# 2단계. 끝 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
# 3단계. (2단계에서 구한 날짜) - (1단계에서 구한 날짜)를 구합니다.
# 시작 날짜의 월, 일을 나타내는 startmonth, startday, 끝 날짜의 월, 일을 나타내는 endmonth, endday가 매개변수로 주
# 어질 때, 시작 날짜와 끝 날짜가 며칠만큼 떨어져 있는지 return 하도록 solution 함수를 작성했습니다. 이때, 위 구조를 참
# 고하여 중복되는 부분은 func_a라는 함수로 작성했습니다. 코드가 올바르게 동작할 수 있도록 빈칸을 알맞게 채워주세요.


def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    for i in range(month-1):
        total += month_list[i]
    total += day
    return total - 1
        
def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")