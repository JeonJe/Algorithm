# 어떤 자리 수 k 가 주어졌을 때 각 자릿수의 k 제곱의 합이 원래 수가 되는 수를 자아도취 수라고 합
# 니다 . 예를 들어 153 은 세 자리 자아도취 수입니다
# 자연수 k 가 매개변수로 주어질 때 ,
# k 자리 자아도취 수들을 리스트에 오름차순으로 담아 return 하도
# 록 solution 함수를 작성하려 합니다 . 빈칸을 채워 전체 코드를 완성해주세요

def power(base, exponent):
    val = 1
    for i in range(exponent):
        val *= base
    return val

def solution(k):
    answer = []
    bound = power(10, k)   # 10 ^ 3
    for i in range(bound // 10, bound):  # 100 ~ 999
        current = i
        calculated = 0

        while current != 0:
           calculated += power(current %10, 3)
           current = current// 10

        if calculated == i:  # 자아 도취 확인
            answer.append(i)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
k = 3
ret = solution(k)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")