# 체스에서
# 비숍 ( 은 아래 그림과 같이 대각선 방향으로 몇 칸이든 한 번에 이동할 수 있습니다 .
# 만약 , 한 번에 이동 가능한 칸에 체스 말이 놓여있다면 그 체스 말을 잡을 수 있습니다
# 8 x 8
# 크기의 체스판 위에 여러 개의 비숍 ( 이 놓여있습니다 . 이때 , 비숍 ( 들에게 한 번에
# 잡히지 않도록 새로운 말을 놓을 수 있는 빈칸의 개수를 구하려고 합니다
# https://grepp
# programmers.s3.amazonaws.com/files/ybm/07fd25eb65/561e9310 6ee3 4ecf
# 85bd dd573bdbb8df.png
# 위
# 그림에서 원이 그려진 칸은 비숍에게 한 번에 잡히는 칸들이며 , 따라서 체스 말을 놓을 수 있는 빈
# 칸 개수는 50 개입니다
# 8 x 8
# 체스판에 놓인 비숍의 위치 bishops 가 매개변수로 주어 질 때 , 비숍에게 한 번에 잡히지 않도록
# 새로운 체스 말을 놓을 수 있는 빈칸 개수를 return 하도록 solution 함수를 완성해주세요

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")