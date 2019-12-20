# 1 이상 9 이하 숫자가 적힌 카드를 이어 붙여 숫자를 만들었습니다 . 이때 , 숫자 카드를 조합해 만든
# 수 중에서 n 이 몇 번째로 작은 수인지 구하려 합니다
# 예를 들어 , 숫자 카드 1, 2, 1, 3 로 만들 수 있는 수를 작은 순으로 나열하면 [1123, 1132, 1213,
# 1231, 1312, ... , 3121, 3211] 입니다 . n 이 1312 라면 , 숫자 카드를 조합해 만든 수 중 n 은 n 은 5 번
# 째로 작은 수입니다
# 숫자 카드를 담은 리스트 card, 수 n 이 매 개변수로 주어질 때 숫자 카드를 조합해 만든 수 중에서 n
# 이 몇 번째로 작은 수인지 return 하도록 solution 함수를 완성해주세요

import  itertools

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    answer = 0
    arr =[]
    temp = sorted(list(itertools.permutations(card,len(card))))

    for i in range(len(temp)):
        new_num = ''
        flag = True

        for j in range(len(temp[i])): # 현재 문자열
            new_num+=str(temp[i][j])

        new_num = int(new_num)
        for d in arr:

            if d==new_num:
                flag=False

        if flag == True:
             arr.append(new_num)

    print (arr,n)
    if arr.count(n)!=0:
        return arr.index(n)+1
    else:
        return -1

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")