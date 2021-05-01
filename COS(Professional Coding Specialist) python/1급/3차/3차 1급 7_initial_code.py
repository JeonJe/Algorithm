# 카프리카 수는 다음을 만족하는 수를 뜻합니다
# *자신의 제곱수를 둘로 나누어 더한 값이 자기 자신과 같습니다
# *단 , 둘로 나뉜 수는 모두 양수여야 합니다
# 예를들어 , 55^2 는 3,025 입니다 . 3,025 는 3 과 025, 30 과 25, 302 와 5 로 나눌 수 있습니다 . 이
# 때 30+25 = 55 이므로 55 는 카프리카 수입니다
# 자연수k 가 매개변수로 주어질 때 , k 이하인 모든 카프리카 수를 리스트에 담아 오름차순으로 정렬하
# 여 return 하도록 solution 함수를 작성했습니다 . 그러나 , 코드 일부분이 잘못되었기 때문에 , 코드가
# 올바르게동작하지 않습니다 . 주어진 코드에서 한 줄 만 변경해 모든 입력에 대 해 올바르게 동작하도록
# 수정해주세요
def solution(k):
    answer = []
    for i in range(1, k + 1):
        square_num = i * i
        divisor = 1
        while square_num // divisor != 0: # 여기 수정
            front = square_num // divisor
            back = square_num % divisor
            divisor *= 10
            if back != 0 and front != 0:
                if front + back == i:
                    answer.append(i)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
k = 500
ret = solution(k)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")