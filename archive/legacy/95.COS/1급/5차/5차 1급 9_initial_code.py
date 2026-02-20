# 정수 # number 와 target 이 주어졌을 때 ,
# 다음 세 연산을 이용해 number 를 target 으로 만들려 합니다
# ```
# 연산
# 1. 1 을 더합니다 연산
# 2. 1 을 뺍니다 연산
# 3. 2 를 곱합니다 ```
# 정수 number 와 target 이 매개변수로 주어질 때 , number 로 target 으로 만들려면 연산을 최소 몇 번
# 해야 하는지 return 하도록 solution 함수를 작성해 주세요
import queue

def solution(number, target):
    #여기에 코드를 작성해주세요.
    answer = 0
    visited = [0 for _ in range(10001)]
    q = queue.Queue()
    q.put(number)
    visited[number]=1
    cnt  = 0
    while q.empty()==False:
        f = q.get()  # 현재 값 가져옴

        if f == target: # 현재 값이 타겟넘버면?
            break

        if f + 1 <= 10000 and visited[f + 1] == 0:
            visited[f + 1] = visited[f] + 1  # 몇번의 연산으로 해당 값이 만들어졌는지
            q.put(f + 1)

        if f - 1 >= 0 and visited[f - 1] == 0:
            visited[f - 1] = visited[f] + 1
            q.put(f - 1)

        if 2 * f <= 10000 and visited[2 * f] == 0:
            visited[2 * f] = visited[f] + 1
            q.put(f * 2)

    return visited[target]-1

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")