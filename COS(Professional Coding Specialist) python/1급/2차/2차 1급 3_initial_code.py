# 문제
# 설명
# A
# 사이트에서 아래 조건에 맞는 게시글을 최초 로 작성하는 이용자에게 경품을 제공하려 합니다
#  현재 작성되어 있는 가장 마지막 게시글 이후에 작성된 게시글이어야 합니다
#  게시글 번호의 자릿수가 짝수여야 합니다
#  게시글 번호가 2n 자릿수 일때 , 앞 n 자리의 각 자릿수의 합과 뒤 n 자리의 각 자릿수의 합
# 이 같아야 합니다
# 이
# 사이트의 게시글 번호는 마지막에 작성된 게시글 번호부터 1 씩 증가합니다 . 예를 들어 , 가장 마지
# 막 게시글의 번호가 235386 이라면 , 이후에 작성되는 게시글의 번호는 235387, 235388 ... 이 되며 ,
# 번호가 235387 이상인 게시글이 경품당첨의 대상이 됩니다
# 당신은
# 경품을 받기위해 앞으로 게시글을 몇 개 더 작성해야 하는지 구하려 합니다 . 이를 위해 다음과
# 같이 프로그램 구조를 작성했습니다
# 1.
# 게시글 번호를 1 증가시키고 자릿수를 구합니다
# 2.
# 만약 자릿수가 짝수가 아니라면 1 로 돌아갑니다
# 3.
# 만약 구한 자릿수가 짝수라면 다음을 수행합니다
# 3 1. 앞 자릿수 절반과 뒷 자릿수 절반을 분리합니다
# 3 2. 앞 자릿수 절반의 자릿수 합과 뒷 자릿수 절반의 자릿수 합을 구합니다
# 3 3. 위에서 구한 합이 서로 같으면 4 로 가고 , 같지 않으면 1 로 돌아갑니다
# 4. (3
# 에서 구한 수 처음에 매개변수로 주어진 수 를 return 합니다
# 가장
# 마지막 게시글의 번호 num 이 매개변수로 주어질 때 , 경품을 받기 위해 앞으로 더 작성해야 하
# 는 게시글의 개수를 return 하도록 solution 함수를 작성하려 합니다 . 위 구조를 참고하여 코드가 올
# 바르게 동작할 수 있도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세
# 요
def func_a(n):
    ret = 1
    while n > 0:
        ret *= 10
        n -= 1
    return ret

def func_b(n):
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret

def func_c(n):
    ret = 0
    while n > 0:
        ret += n%10
        n //= 10
    return ret

def solution(num):
    next_num = num
    while True:
        next_num += 1 # 게시글 번호를 1 증가시키고
        length = func_b(next_num) # 자리수 구하기 O
        if length % 2:
            continue
        
        divisor = func_a(length//2)  # 앞 자리수 절반과 뒷 자리 절반 분리하기
        front = next_num // divisor  # 6자리 일경우 func_a(3) : 10 -> 100-> 1000 이 divisor가 됨
        back = next_num % divisor
        
        front_sum = func_c(front)
        back_sum = func_c(back)
        if front_sum == back_sum:
            break
            
    return next_num - num

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 1
ret1 = solution(num1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")