# 자연수가
# 중복 없이 들어있는 리스트가 있습니다 . 이 리스트에서 합이 K 의 배수가 되도록 서로 다른
# 숫자 세 개를 고르는 방법은 몇 가지인지 세려고 합니다
# 자연수가
# 들어있는 리스트 arr 가 매개변수로 주어질 때 , 이 리스트에서 합이 K 의 배수가 되도록 서로
# 다른 숫자 세 개를 고르는 방법의 가짓수를 return 하도록 solution 함수를 완성해주세요

def check_multi(sum,K):
    i = 1
    while(K*i<=1000):
        if K*i == sum:
            return True
        i+=1
    return False

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0
    size = len(arr);
    for i in range(size):
        for j in range(i+1,size):
            for k in range(j+1,size):
                sum = arr[i] + arr[j] + arr[k]
                if(check_multi(sum,K)):
                    answer+=1

    # 합이 K 의 배수가 되도록 서로 다른 숫자 세 개를 고르는 방법의 가짓수를 return 해주세
    # 요
    # 방법이 없다면 0 RETURN
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")