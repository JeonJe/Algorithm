# 알파벳 문자열이 주어질 때, 연속하는 중복 문자를 삭제하려고 합니다. 예를 들어, "senteeeencccccceeee"라는 문자열
# 이 주어진다면, "sentence"라는 결과물이 나옵니다.
# 영어 소문자 알파벳으로 이루어진 임의의 문자열 characters가 매개변수로 주어질 때, 연속하는 중복 문자들을 삭제한 결
# 과를 return 하도록 solution 함수를 작성하였습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 코드가 올바르게 동작
# 하지 않습니다. 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

def solution(characters):
    result = ""
    result += characters[0]   #처음 글자 추가
    for i in range(1,len(characters)):
        if characters[i - 1] != characters[i]: #이전 문자와 같지 않으면 ? 중복아님
            result += characters[i]
    return result

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
characters = "senteeeencccccceeee"
ret = solution(characters)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")