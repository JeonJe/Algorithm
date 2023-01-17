# hour 시 minute 분에 아날로그 시계의 시침과 분침이 몇 도를 이루는지 계산하려 합니다 . 예를 들어 ,
# 3 시 00 분에 시침과 분침은 90˚ 를 이룹니다
# 어떤 시점의 시 hour, 분 minute 이 매개변수로 주어질 때 , hour 시 minute 분에 아날로그 시계의 시
# 침과 분침이 이루는 각도를 소숫점 첫번째 자리까지 표현한 문자열을 return 하도록 solution 함수를 작성해주세요


# 시침은 1시간에 360 / 12 = 30도씩
# 분침은 1분 360 / 60 = 6도
# 시침이 1시간에 30도 움직이고 분침이 60분 지나면 30도 움직이니까
# 30 / 60 => 시침은 1분에 0.5도

def solution(hour, minute):
    answer = ''
    r_hour = 30*hour +minute*0.5
    r_minute = 6*minute

    answer = abs(r_hour - r_minute)
    if answer > float(360) - answer:
        answer = float(360) - answer
    return "{0:.1f}".format(answer)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 0
minute = 59

ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")