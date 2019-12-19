# 모 매장에서는 팝업스토어를 열려고 합니다 . 팝업스토어란 한정 기간 문을 여는 매장입니다 . 팝업스토
# 어는 k 일 동안 연속해서 열 예정입니다 . n 일 동안의 추정 매출액이 주어질 때 , 언제 팝업스토어를 열
# 어야 가장 매출이 높을지 알아보려 합니다
# n 일 간의 추정 매출액이 담긴 리스트 revenue 와 팝업스토어를 열 날의 수 k 가 매개변수로 주어질
# 때 , 최대 매출액 합을 return 하도록 solution 함수를 작성했습니다 . 그러나 , 코드 일부분이 잘못되어
# 있기 때문에 , 몇몇 입력에 대해서는 올바르게 동작하지 않습니다 . 주어진 코드에서 한 줄 만 변경해서
# 모든 입력에 대해 올바르게 동작하도록 수정하세요

def solution(revenue, k) :
    answer = 0
    rsum = sum(revenue[0:k])  # 처음 k 일동안
    answer = rsum
    for i in range(len(revenue)) :
        rsum = rsum + revenue[i - k] - revenue[i]
        if answer < rsum :
            answer = rsum
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
revenue1 = [1, 1, 9, 3, 7, 6, 5, 10]
k1 = 4
ret1 = solution(revenue1, k1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

revenue2 = [1, 1, 5, 1, 1]
k2 = 1
ret2 = solution(revenue2, k2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")