# 369 게임은 여러 명이 같이하는 게임입니다. 게임의 규칙은 아래와 같습니다. * 1부터 시작합니다. * 한 사람씩 차례대로 숫
# 자를 1씩 더해가며 말합니다. * 말해야 하는 숫자에 3, 6, 9중 하나라도 포함되어있다면 숫자를 말하는 대신 숫자에 포함된
# 3, 6, 9의 개수만큼 손뼉을 칩니다.
# 어떤 수 number가 매개변수로 주어질 때, 1부터 number까지 369게임을 올바르게 진행했을 경우 박수를 총 몇 번 쳤는지
# 를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            if current%10 ==3  or current%10 == 6 or current%10 == 9: #각자리
                count += 1
            current = current // 10   # 다음 digit
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number = 40
ret = solution(number)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
