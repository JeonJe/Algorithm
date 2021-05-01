# p 진법으로 표현한 수란 , 각 자리를 0 부터 p 1 의 숫자로만 나타낸 수를 의미합니다 . p 진법으로 표현
# 한 자연수 두개를 더한 결과를 q 진법으로 표현하려 합니다
# 예를 들어 , 3 진법 수 112001 과 12010 을 더한 결과를 8 진법으로 나타내면 1005 입니다
# solution 함수의 매개변수로 p 진법 자연수를 담은 문자열 s1, s2 와 두 수를 나타내는 진법의 기수 p,
# 두 수의 덧셈 결과를 표현할 진법의 기수 q 가 매개변수로 주어집니다 . p 진법으로 표현된 두 수를 더한
# 결과를 q 진법으로 나타낸 값을 return 하도록 solution 함수를 완성해주세요

def conv(number, base):
    T = "0123456789ABCDEF"
    i, j = divmod(number, base)  # 몫과 나머지

    if i == 0:  # 몫이 0이라면 T[나머지]
        return T[j]
    else:
        return conv(i, base) + T[j] #나눠지지 않았다면 몫으로 다시 나누고 나머지 더함


def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.
    answer = ''

    temp = int(s1,p) + int(s2,p) # p진법의 수를 10진수로 변환하고 더함
    answer = conv(int(temp),q) # 10진법의 수를 q 진법의 수로 변환
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")