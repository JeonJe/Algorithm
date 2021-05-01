# UP AND DOWN게임은 다음과 같은 규칙에 따라 진행하는 게임입니다
# *
# 먼저 출제자가 1 이상 ~ K 이하인 자연수 중 하나를 마음속으로 생각합니다
# 게임 참가자는 1 이상 ~ K 이하인 자연수 중 아무거나 하나를 말합니다
# * 만약 , 참가자가 말한 숫자가 출제자가 생각한 숫자보다 작다면 출제자는 "UP" 이라고 말합니다
# * 만약 , 참가자가 말한 숫자가 출제자가 생각한 숫자보다 크다면 출제자는 "DOWN" 이라고 말합니다
# *
# 참가자는 출제자가 말하는 "UP", "DOWN" 힌트 를 잘 활용해서 출제자가 처음에 생각한 숫자를 맞추면 됩니다
# 출제자가 처음에 생각할 수 있는 자연수 범위 K, 게임 참가자가 말한 숫자가 순서대로 담긴 리스트
# numbers, 게임 출제자가 참가자가 말한 각 숫자에 대해 답한 내용이 순서대로 담긴 리스트
# up_down 이 매개변수로 주어집니다 . 리스트에 주어진 순서대로 게임이 진행됐다고 했을 때 , 현재 정
# 답이 될 수 있는 숫자는 몇 개인지 return 하도록 solution 함수를 작성하려 합니다 . 빈칸 을 채워 전
# 체 코드를 완성해주세요

def solution(K, numbers, up_down):
    left = 1
    right = K  # K 이하 자연수
    for num, word in zip(numbers, up_down):
        if word == "UP":
            left = max(left,num+1) # 말한 숫자 + 1
        elif word == "DOWN":
            right = min(right,num-1) #말한 숫자 - 1
        elif word == "RIGHT":
            return 1

    return right-left+1

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K1 = 10
numbers1 = [4, 9, 6]
up_down1 = ["UP", "DOWN", "UP"]
ret1 = solution(K1, numbers1, up_down1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

K2 = 10
numbers2 = [2, 1, 6]
up_down2 = ["UP", "UP", "DOWN"]
ret2 = solution(K2, numbers2, up_down2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

K3 = 100
numbers3 = [97, 98]
up_down3 = ["UP", "RIGHT"]
ret3 = solution(K3, numbers3, up_down3)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")