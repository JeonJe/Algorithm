# 이
# 로봇은 x 축 방향 , 혹은 y 축 방향으로만 움직일 수
# 있으며 , 알파벳으로 명령을 내릴 수 있습니다 . 명령을
# 내릴 때 사용하는 알파벳은 'L', 'R', 'U', ' 의 4 가지
# 이며 , ' 은 x 축 방향으로 1 만큼 , ' 은 x 축 방향으로
# +1 만큼 , ' 는 y 축 방향으로 +1 만큼 , ' 는 y 축 방향
# 으로 1 만큼 이동하라는 의미입니다 .
# 로봇에게
# 내린 명령이 순서대로 들어있는 문자열
# commands 가 매개변수로 주어질 때 , 주어진 명령을
# 모두 수행한 후의 로봇 위치를 return 하도록
# solution 함수를 완성해주세요

def solution(commands):
    # 여기에 코드를 작성해주세요.
    x,y = 0, 0
    answer = []
    for d in commands:
        if d=="U":
            y+=1
        elif d=="D":
            y-=1
        elif d=="L":
            x-=1
        elif d=="R":
            x+=1

    answer.append(x)
    answer.append(y)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")