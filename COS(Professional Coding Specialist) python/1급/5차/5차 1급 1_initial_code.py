# 계단 n 칸을 올라가는 방법의 수를 구하려고 합니다 . 계단은 한 번에 1 계단 , 2 계단 , 3 계단씩 오를 수
# 있습니다
# 예를 들어 , 계단 3 칸을 오르는 방법은 다음과 같이 4 가지가 있습니다
# ```
# 1. 1 계단 + 1 계단 + 1 계단
# 2. 1 계단 + 2 계단
# 3. 2 계단 + 1 계단
# 4. 3 계단
# ```
# 계단 수 n 이 매개변수로 주어질 때 , 계단을 오르는 경우의 수를 return 하도록 solution 함수를 작성
# 하려 합니다 . 빈칸을 채워 전체 코드를 완성해주세요

def solution(n):
	answer = 0
	steps = [0 for _ in range(n+1)]
	steps[1] = 1
	steps[2] = 2
	steps[3] = 4
	for i in range(4, n+1):
		steps[i] = steps[i-3] + steps[i-2] + steps[i-1]

	#3칸전에서 오를 경우 + 2칸전에서 오를 경우 + 1칸 전에서 오를 경우
	answer = steps[n]
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 8
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 4
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")