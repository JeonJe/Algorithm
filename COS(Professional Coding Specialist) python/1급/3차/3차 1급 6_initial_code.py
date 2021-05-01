# 어떤 수를 서로 다른 소수 3 개의 합으로 표현하는 방법의 수를 구하려 합니다
# 예를 들어 33 은 총 4 가지 방법으로 표현할 수 있습니다
#
# 자연수  n 이 매개변수로 주어질 때 , n 을 서로 다른 소수 3 개의 합으로 표현하는 방법의 수를 return
# 하도록 solution 함수를 작성하려 합니다 . 빈칸을 채워 전체 코드를 완성해주세요
# ※ 1,000 이하인 소수는 168 개 있습니다

def solution(n):
    answer = 0
    primes = [2]
    for i in range (3, n + 1, 2) :
        is_prime = True
        for j in range(2, i) :
            if i % j == 0 :
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)

    prime_len = len(primes)
    for i in range(0, prime_len - 2) :
        for j in range(i + 1, prime_len - 1) :
            for k in range(j + 1, prime_len) :
                if primes[i]+primes[j]+primes[k] == n :
                    answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 33
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 9
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")