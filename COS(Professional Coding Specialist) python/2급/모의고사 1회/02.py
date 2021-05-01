#A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다. 회원 등급에 따른 할인율은 다음과 같습니다. (S = 실버, G =
#골드, V = VIP)
# S" 5%, "G" 10%, "V" 15%
#상품의 가격 price와 구매자의 회원 등급을 나타내는 문자열 grade가 매개변수로 주어질 때, 할인 서비스를 적용한 가격을
#return 하도록 solution 함수를 완성해주세요.
#할인한 가격을 return 하도록 solution 함수를 작성해주세요.

#import math

def solution(price, grade):
    # 여기에 코드를 작성해주세요.
    answer = 0
    if grade == "V":
        answer = price * 0.85
    elif grade == "G":
        answer = price * 0.90
    elif grade == "S":
        answer = price * 0.95

    return int(answer)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")