# A마트에서 각티슈 1개와 두루마리 휴지 3개를 한 세트로 판매하려고 합니다. 그런데, 종류에 상관
# 없이 물품을 n개 남겨서 낱개로 판매하려고 합니다. 세트는 최대한 많이 만들려고 합니다.
# 각티슈의 개수 tissue와 두루마리 휴지의 개수 scroll, 남길 물품의 개수 n이 매개변수로 주어졌을
# 때 최대로 만들 수 있는 세트의 개수를 return 하도록 solution 함수를 작성했습니다. 그러나, 코
# 드 일부분이 잘못되어 있기 때문에 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코
# 드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

def solution(tissue, scroll, n):
    answer = 0
    
    if scroll < tissue * 3:
        answer = scroll // 3
    else:
        answer = tissue    

    tissue -= answer
    scroll -= answer * 3

    i = 0
    while n - (tissue + scroll + i) > 0:
        if i % 4 == 0:
            answer += 1
        i = i + 1
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
tissue1 = 2
scroll1 = 5
n1 = 2
ret1 = solution(tissue1, scroll1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

tissue2 = 5
scroll2 = 20
n2 = 4
ret2 = solution(tissue2, scroll2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
