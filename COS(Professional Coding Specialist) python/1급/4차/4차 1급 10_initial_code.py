# 자연수를 제곱한 수는 제곱수 , 세 제곱한 수는 세제곱 수라고 합니다 . 예를 들어 2^2 = 4 는 제곱수 ,
# 3^3 = 27 은 세제곱수 입니다
# 두 자연수 a, b 가 주어질 때 a 이상 b 이하인 자연수 중 소수 의 제곱수와 세제곱수의 개수를 구하려
# 합니다 . 예를 들어 a = 6, b = 30 일 때 소수의 제곱수는 [9, 25]로 2 개 , 소수의 세제곱수는 [8,27] 로
# 2 개로 총 4 개입니다
# 두 자연수 a, b 가 매개변수로 주어질 때 , a 이상 b 이하인 제곱수와 세제곱수의 개수의 합을 return
# 하도록 solution 함수를 완성해주세요

def solution(a, b):  # b가 1 000 000 000 일 때
    # 여기에 코드를 작성해주세요.
    answer = 0
    prime =[]
    visit = [False] * (b+1)

    for i in range(2,b+1):
        if(visit[i]==False):
            prime.append(i)
        for j in range(i,b+1,i):
            visit[j] = True

    for i in prime:
        if a<=i*i<=b:
            answer +=1
        if a<=i*i*i<=b:
            answer+=1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  100000
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")