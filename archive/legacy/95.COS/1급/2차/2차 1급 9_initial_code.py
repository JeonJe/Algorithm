# 문제# 설명
# 주어진 비밀번호가 안전한지 아닌지 판단하려 합니다 . 비밀번호의 안전 여부는 다음 규칙으로 판단합니다
#  연속된 3 자리 이상의 알파벳 혹은 숫자를 사용할 수 없습니다 . abc, cba, 012, 987 등
# 비밀번호에 사용할 문자열 password 가 매개변수로 주어질 때 , 주어진 문자열이 위 규칙에 맞으면
# true 를 , 맞지 않으면 false 를 return 하도록 solution 함수를 작성했습니다 . 그러나 , 코드 일부분이 잘
# 못되어있기 때문에 , 몇몇 입력에 대해서는 올바르게 동작하지 않습니다 . 주어진 코드에서 한 줄 만 변
# 경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요


def solution(password):
    length = len(password)
    for i in range(length - 2):
        first_check = ord(password[i + 1]) - ord(password[i])
        second_check = ord(password[i+2]) - ord(password[i+1])  #여기 수정
        # print(password[i + 1],password[i],password[i+1],second_check)
        if first_check == second_check and (first_check == 1 or second_check == -1):
            return False
    return True

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
password1 = "cospro890"
ret1 = solution(password1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "kjsdnt123os"
ret2 = solution(password2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")