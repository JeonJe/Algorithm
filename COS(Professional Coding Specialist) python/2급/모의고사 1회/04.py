# 자연수가 들어있는 리스트가 있습니다. 이 리스트에서 가장 많이 등장하는 숫자의 개수는 가장 적게 등장하는 숫자 개수의
# 몇 배인지 구하려 합니다. 이를 위해 다음과 같이 간단히 프로그램 구조를 작성했습니다.
# 1단계. 리스트에 들어있는 각 자연수의 개수를 셉니다.
# 2단계. 가장 많이 등장하는 수의 개수를 구합니다.
# 3단계. 가장 적게 등장하는 수의 개수를 구합니다.
# 4단계. 가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇 배 더 많은지 구합니다.
# 단, 몇 배 더 많은지 구할 때는 소수 부분은 버리고 정수 부분만 구하면 됩니다.
# 자연수가 들어있는 리스트 arr가 매개변수로 주어질 때, 가장 많이 등장하는 숫자가 가장 적게 등장하는 숫자보다 몇 배 더
# 많은지 return 하도록 solution 함수를 작성하려 합니다. 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주
# 어진 funca, funcb, func_c 함수와 매개변수를 알맞게 채워주세요.

def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr): #max
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr): #min
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")