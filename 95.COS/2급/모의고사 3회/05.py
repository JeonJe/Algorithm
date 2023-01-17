# 버스 승객들의 나이를 담고 있는 리스트 age와 버스의 종류인 RGB가 매개변수로 주어질 때 총
# 버스요금을 return 하도록 solution 함수를 작성하려고 합니다. 빈칸을 채워 전체 코드를 완성해
# 주세요.

def solution(age, RGB):
    if RGB == 'R':
        pay1 = 0
        pay2 = 1200
        pay3 = 1800
        pay4 = 2400
    elif RGB == 'G':
        pay1 = 0
        pay2 = 400
        pay3 = 800
        pay4 = 1200
    elif RGB == 'B':
        pay1 = 0
        pay2 = 500
        pay3 = 1000
        pay4 = 1300

    if len(age) >= 10:
        pay2 = pay2 * 0.95
        pay3 = pay3 * 0.9
        pay4 = pay4 * 0.8

    pay = 0
    for a in age:
        if a<8:
            pay += pay1
        elif 8<=a<13:
            pay += pay2
        elif 13<=a<20:
            pay += pay3
        else:
            pay += pay4

    return int( pay )


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
age1 = [18, 23, 70, 10, 5, 13]
RGB1 = "B"
ret1 = solution(age1, RGB1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

age2 = [18, 23, 70, 10, 5, 13, 11, 27,
        77, 56, 7, 19, 25, 52, 31, 8]
RGB2 = "R"
ret2 = solution(age2, RGB2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
