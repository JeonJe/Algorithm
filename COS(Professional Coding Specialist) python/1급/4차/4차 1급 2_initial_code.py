# 알파벳 소문자와 대문자로 구성된 문자열을 압축하려 합니다 . 압축이란 대표 문자와 대표 문자가 연속
# 되는 개수를 함께 표현하는 것입니다 . 이때 , 대문자와 소문자는 구분하지 않으며 , 대표 문자는 소문자
# 로 표현합니다
# 예를 들어 , 문자열 " 을 압축하면 " 입니다
# 문자열 s 가 매개변수로 주어질 때 , s 를 압축한 문자열을 return 하도록 solution 함수를 작성했습 니다 .
# 그러나 , 일부 코드가 잘못되어 코드가 바르게 동작하지 않습니다 . 주어진 코드가 모든 입력을 바르게
# 처리하도록 코드를 수정해주세요 . 코드는 한 줄 만 수정해야 합니다

def solution(s):
    s = s.lower()
    answer = ""
    previous = s[0]
    counter = 1
    for alphabet in s[1:]:
        if alphabet == previous:
            counter += 1
        else:
            answer += previous + str(counter)
            counter = 1
            previous = alphabet
    answer += previous + str(counter)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
s = "YYYYYbbbBbbBBBMmmM"
ret = solution(s)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")