# 공장에서 운동화를 만들고 있습니다. 왼발 운동화를 만드는 제작 라인과 오른발 운동화를 만
# 드는 제작 라인이 별도로 운영되고 있습니다. 왼발 운동화 사이즈가 들어 있는 리스트와 오른
# 발 운동화 사이즈가 들어 있는 리스트가 있습니다. 운동화 사이즈는 210부터 260까지 10단
# 위로 구분됩니다. 사이즈가 같은 경우 왼발 운동화와 오른발 운동화를 합쳐 완제품을 만들 수
# 있습니다. 이때 최대한 많은 완제품을 만들면 최대 몇 켤레를 만들 수 있는지 구하려고 합니
# 다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.
# 1. 왼발 운동화의 사이즈 별로 몇 개씩 있는지 개수를 셉니다.
# 2. 오른발 운동화의 사이즈 별로 몇 개씩 있는지 개수를 셉니다.
# 3. 각 사이즈 별로 최대한 많은 운동화 한 켤레를 만들면서 개수를 셉니다.
# 왼발 운동화의 사이즈가 담긴 리스트 left_shoes와 오른발 운동화의 사이즈가 담긴 리스트
# right_shoes가 매개변수로 주어질 때 최대 몇 켤레의 운동화를 만들 수 있는지 return 하도
# 록 solution 함수를 작성하려 합니다. 이때, 위 구조를 참고하여 중복되는 부분은 func_

size_kinds = 6

def func_a(shoes):
    count = [0 for _ in range(size_kinds)]
    for x in shoes:
        y = 0
        if x==210:
            y = 0
        elif x==220:
            y = 1
        elif x==230:
            y = 2
        elif x==240:
            y = 3
        elif x==250:
            y = 4
        elif x==260:
            y = 5

        count[y] +=1
    return count

def solution(left_shoes, right_shoes):
    left_count = func_a(left_shoes)
    right_count = func_a(right_shoes)
    
    pair = 0
    for i in range(size_kinds):
        pair += min(left_count[i], right_count[i])
    return pair

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_shoes = [210, 210, 220, 220, 230, 230,
              240, 250, 260, 230, 240, 210]

right_shoes = [230, 250, 220, 220, 230, 250,
               210, 230, 240, 250, 230, 240]

ret = solution(left_shoes, right_shoes)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
