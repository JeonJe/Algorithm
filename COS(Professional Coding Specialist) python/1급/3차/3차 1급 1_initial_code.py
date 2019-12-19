# 정수로 이루어진 두 리스트 arrA 와 arrB 가 주어질 때 , arrA 를 회전해 arrB 로 만들 수 있는지 알아보
# 려 합니다 . 리스트의 회전이란 모든 원소를 오른쪽으로 한 칸씩 이동시키고 , 마지막 원소는 리스트의
# 맨 앞에 넣는 것을 말합니다
# ~~~
# 1. arrA
# 와 arrB 의 길이가 다르면 false 를 return 합니다
# 2.
# 두 리스트의 구성 성분이 달라 회전했을 때 같아질 가능성이 없다면 false 를 return 합니다
# 3. arrA
# 리스트를 두 번 이어 붙여 길이가 2 배인 리스트로 만듭니다
# 4. arrA
# 의 부분 리스트 중 arrB 와 같은 리스트가 있으면 true 를 , 그렇지 않으면 false 를 return 합니
# 다
# ~~~
# 두
# 리스트 arrA 와 arrB 가 매개변수로 주어질 때 , arrA 를 회전해 arrB 로 만들 수 있으면 true 를 , 그렇
# 지 않으면 false 를 return 하도록 solution 함수를 작성하려 합니다 . 위 구조를 참고하여 코드가 올바
# 르게 동작할 수 있도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요


def func_a(arr):  #길이가 2배인 리스트로 만든다
    ret = arr + arr
    return ret

def func_b(first, second):
    MAX_NUMBER = 1001
    counter = [0 for _ in range(MAX_NUMBER)]
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    for c in counter:
        if c != 0:
            return False
    return True

def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False

    # 두 리스트의 구성 성분이 달라 회전했을 때 같아질 가능성이 없다면 false 리턴
    if func_b(arrA,arrB):

        arrA_temp = func_a(arrA)
        if func_c(arrA_temp,arrB):
            return True
    return False

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
ret1 = solution(arrA1, arrB1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
ret2 = solution(arrA2, arrB2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")