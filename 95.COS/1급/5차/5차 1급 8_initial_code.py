# 세 수 a, b, c 의 공약수가 몇 개인지 구하려고 합니다 . 공약수란 , 동시에 모든 정수의 약수인 정수를 뜻
# 합니다 . 예를 들어 , 세 수 24, 9, 15 의 공약수는 1, 3 이고 , 따라서 양의 공약수는 2 개입니다
# 세 수의 공약수가 몇 개인지 구하기 위해 다음과 같이 프로그램 구조를 작성했습니다
# ```
# 1. 세 수의 최대공약수를 구합니다
# 2. 앞서 구한 최대공약수의 약수가 몇 개인지 구합니다
# ```
# 세 수 a, b, c 가 매개변수로 주어질 때 , 세 수의 약수가 몇 개인지 return 하도록 solution 함수를 작
# 성하려 합니다 . 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 func_a,
# func_b, func_c 함수와 매개변수를 알맞게 채워주세요

def func_a(a, b):  #최대 공약수
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
	return b

def func_b(n):
	answer = 0
	for i in range(1, n+1): # 최대 공약수의 약수
		if func_c(n,i):
			answer += 1
	return answer

def func_c(p, q):
	if p % q == 0:
		return True
	else:
		return False

def solution(a, b, c):
    answer = 0
    gcd = func_a(func_a(a,b),c)
    answer = func_b(gcd)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a = 24
b = 9
c = 15
ret = solution(a, b, c)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")