# 정확히 n 일 연속으로 스키장 이용하는데 필요한 최소 비용을 계산하려 합니다 . 다음은 스키장에서 판
# 매하는 이용권입니다
# |
# 이용권 종류 | 스키장을 사용할 수 있는 일수 | 가격|
# | one_day |구매한 날 하루 동안 사용 가능 | one_day_price|
# multi_day | 구매한 날부터 multi_day 일간 사용 가능 | multi_day_price
# solution  함수의 매개변수로 one_day_price, multi_day, multi_day_price, n 가 주어집니다 .
# 이때 정확히 n 일 연속 스키장을 이용하는데 필요한 최소 금액을 계산해서 return 하도록 solution 함수를 작성
# 했습니다 . 그러나 , 일부 코드가 잘못되어 코드가 바르게 동작하지 않습니다 . 주어진 코드가 모든 입력
# 을 바르게 처리하도록 코드를 수정해주세요 . 코드는 한 줄 만 수정해야 합니다

def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n // multi_day) * multi_day_price + (n % multi_day) * one_day_price
        
# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
one_day_price1 = 3
multi_day1 = 5
multi_day_price1 = 14
n1 = 6
ret1 = solution(one_day_price1, multi_day1, multi_day_price1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

one_day_price2 = 2
multi_day2 = 3
multi_day_price2 = 5
n2 = 11
ret2 = solution(one_day_price2, multi_day2, multi_day_price2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")