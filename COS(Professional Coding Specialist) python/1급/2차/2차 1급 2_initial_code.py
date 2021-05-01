# 문제
# 설명
# A
# 지하철역의 오늘 하루 지하철 도착 시각이 순서대로 들어있는 리스트가 있습니다 . 현재 시간이 주어
# 졌을 때 , 지하철을 타기위해서는 최소 몇 분을 기다려야 하는지 구하려 합니다 . 이를 위해 다음과 같
# 이 프로그램 구조를 작성했습니다
# 1. 00:00
# 을 기준으로 해서 현재 시각을 분 단위로 변환합니다
# 2.
# 리스트를 순회하며 다음을 수행합니다
# 2 1. 00:00 을 기준으로 , 각 지하철 도착 시각을 분 단위로 변환합니다
# 2 2. 현재 시각과 지하철 도착 시각을 비교하여 최소 대기 시간을 구합니다
# 3. 2
# 번 단계에서 구한 최소 대기 시간을 return 합니다
# 오늘
# 하루 동안의 지하철 도착 시각이 순서대로 들어있는 리스트 subway_times 와 현재시간
# current_time 이 매개변수로 주어질 때 , 지하철을 타기 위해 기다려야 하는 최소 대기 시간을 return
# 하도록 solution 함수를 작성했습니다 . 이때 , 위 구조를 참고하여 중복되는 부분은 func_a 라는 함수로
# 작성했습니다 . 코드가 올바 르게 동작할 수 있도록 빈칸을 알맞게 채워 전체 코드를 완성해주세요


def func_a(times):
    hour = int(times[:2])
    minute = int(times[3:])
    return hour*60 + minute

def solution(subway_times, current_time):
    current_minute = func_a(current_time)
    INF = 1000000000
    answer = INF
    for s in subway_times:
        subway_minute = func_a(s)
        if current_minute <= subway_minute:
            answer = subway_minute - current_minute
            break
    if answer == INF:
        return -1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.

subway_times1 = ["05:31", "11:59", "13:30", "23:32"]
current_time1 = "12:00"
ret1 = solution(subway_times1, current_time1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

subway_times2 = ["14:31", "15:31"]
current_time2 = "15:31"
ret2 = solution(subway_times2, current_time2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")