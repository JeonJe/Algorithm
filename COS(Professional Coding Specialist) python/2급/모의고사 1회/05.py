# 주어진 리스트의 순서를 뒤집으려고 합니다.
# 예를 들어 주어진 리스트가 [1, 4, 2, 3]이면, 순서를 뒤집은 리스트는 [3, 2, 4, 1]입니다.
# 매개변수 설명
# return 값 설명
# 예시
# 예시 설명
# 문제5
# 정수가 들어있는 리스트 arr가 매개변수로 주어졌을 때, arr를 뒤집어서 return 하도록 solution 함수를 작성하려 합니다.
# 빈칸을 채워 전체 코드를 완성해주세요.
def solution(arr):
    left, right = 0, len(arr)-1
    while left<=right :
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 4, 2, 3,5,7,8,10]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")