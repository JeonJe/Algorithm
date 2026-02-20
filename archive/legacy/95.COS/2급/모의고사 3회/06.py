# G고등학교의 A선생님이 수업하는 교실은 1층부터 4층 사이에 있습니다. 선생님이 하룻동안 수
# 업하고 이동하는 교실의 층이 담긴 리스트가 있습니다. 하루 동안 선생님이 이동한 총 층의 수를
# 구하려고 합니다.
# 예를 들어 리스트 [1, 2, 4, 3, 1, 4, 2, 1]가 주어진다면, 선생님이 이동한 총 층은 12층입니다.
# 하루 동안 수업하고 이동하는 교실의 층이 담긴 리스트 floors가 매개변수로 주어질 때 선생님이
# 이동한 층의 총 수를 return하도록 solution 함수를 작성하겠습니다. 빈칸을 채원 전체 코드를
# 완성해 주세요.

def solution(floors):
    move_floor = 0
    length = len(floors)
    for i in range(1,length):
        if floors[i] > floors[i-1] :
            move_floor += floors[i] - floors[i-1]
        else:
            move_floor += floors[i-1] - floors[i]
    return move_floor

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
floors = [1, 2, 4, 3, 1, 4, 2, 1]
ret = solution(floors)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
