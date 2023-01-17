# 앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어 또는 문장을 팰린드롬(palindrome)이라고 합니다. 예를 들어서
# racecar, noon은 팰린드롬 단어입니다.
# 소문자 알파벳, 공백(" "), 그리고 마침표(".")로 이루어진 문장이 팰린드롬 문장인지 점검하려 합니다. 문장 내에서 알파벳만
# 추출하였을 때에 팰린드롬 단어이면 팰린드롬 문장입니다. 예를 들어, "Never odd or even."과 같은 문장은 팰린드롬입니
# 다.
# 소문자 알파벳, 공백(" "), 그리고 마침표(".")로 이루어진 문장 sentence가 주어질 때 팰린드롬인지 아닌지를 return 하도
# 록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지
# 않습니다. 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.

def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True


#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
sentence1 = "never odd or even."
ret1 = solution(sentence1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")
    
sentence2 = "palindrome"
ret2 = solution(sentence2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")