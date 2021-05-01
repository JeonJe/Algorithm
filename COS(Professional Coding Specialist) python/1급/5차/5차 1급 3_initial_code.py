# 서로 다른 정수 n 개가 담긴 리스트가 있습니다 . 이 리스트를 앞 `(n+1)/ 개 원소는 증가하고 뒤
# `(n+1)/ 개 원소는 감소하도록 정렬하려고 합니다 . 이때 , 조건을 만족하는 리스트가 여럿인 경우 사전
# 순으로 가장 먼저 나오는 리스트를 답으로 합니다 . 예를 들어 , 주어진 리스트가 [7, 3, 4, 1, 2, 5, 라
# 면 정렬한 이후에는 [1, 2, 3, 7, 6, 5, 가 됩니다
# 정수 리스트가 numbers 가 매개변수로 주어질 때 , 문제의 조 건에 맞게 정렬하여 return 하도록
# solution 함수를 작성했습니다 . 그러나 , 코드 일부분이 잘못되어있기 때문에 , 몇몇 입력에 대해서는 올
# 바르게 동작하지 않습니다 . 주어진 코드에서 한 줄 만 변경해서 모든 입력에 대해 올바르게 동작하도록
# 수정하세요

def solution(numbers):
    answer = []
    numbers.sort()
    mid = (len(numbers) - 1) // 2
    numbers[mid], numbers[len(numbers) - 1] = numbers[len(numbers) - 1], numbers[mid]

    left = mid + 1
    right = len(numbers) - 2  # 여기 -1 에서 -2 로 수정

    while left <= right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left = left + 1
        right = right - 1

    answer = numbers
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
numbers = [7, 3, 4, 1, 2, 5, 6]
ret = solution(numbers)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
