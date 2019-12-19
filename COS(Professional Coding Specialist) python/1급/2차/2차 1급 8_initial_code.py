# 문제
# 설명
# 자연수가
# 들어있는 리스트가 주어질 때 , 다음 규칙에 따라 새로운 리스트를 만들려고 합니다
#  주어진 리스트의 첫 번째 원소를 새로운 리스트의 첫 번째 원소에 넣습니다
#  주어진 리스트의 마지막 원소를 새로운 리스트의 두 번째 원소에 넣습니다
#  계속해서 주어진 리스트의 남아있는 원소 중 가장 앞에 있는 원소와 가장 뒤에 있는 원소를
# 번갈아 가져와 새로운 리스트에 순서대로 넣습니다
#  주어진 리스트에 더이상 원소가 남아있지 않을 때까지 위 과정을 반복합니다
# 자연수가 들어있는 리스트 arr 가 매개변수로 주어질 때 , 위 과정을 수행해서 만든 새로운 리스트를
# return 하도록 solution 함수를 작성했습니다 . 그러나 , 코드 일부분이 잘못되어있기 때문에 , 몇몇 입력
# 에 대해서는 올바르게 동작하지 않습니다 . 주어진 코드에서 한 줄 만 변경해서 모든 입력에 대해 올바
# 르게 동작하도록 수정하세요

def solution(arr):
    left, right = 0, len(arr) - 1
    idx = 0
    answer = [0 for _ in range(len(arr))]
    while left <= right:
        if idx % 2 == 0:
            answer[idx] = arr[left]
            left += 1
        else:
            answer[idx] = arr[right]
            right -= 1
        idx += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
arr = [1, 2, 3, 4, 5, 6]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")