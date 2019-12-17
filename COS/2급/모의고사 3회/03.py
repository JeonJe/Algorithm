# 체조 경기를 진행하고 있습니다. 지금 연기한 선수의 연기 완성도를 채점하는 E점수를 결정하려고
# 합니다. E심판은 모두 6명이며, 각 심판들은 100점 만점에서 시작하여 실수에 따라 점수를 감점합
# 니다. E심판의 점수 중 최고점과 최저점을 제외하고 나머지 심판들의 점수 평균을 최종 E점수로
# 정합니다. 단, 이때 소수점 이하는 버립니다.
# 예를 들어 6명의 E심판이 채점한 점수가 [90, 80, 70, 85, 100, 90]라면, 가장 높은 점수인 100점
# 과 가장 낮은 점수인 70점을 제외하고 나머지 점수의 평균을 구하게 되면 85점입니다. 소수점 이
# 하를 버리게 되면 85점이 최종 점수가 됩니다.
# E심판이 채점한 점수가 담긴 리스트 scores가 매개변수로 주어질 때 최종 E점수를 return하도록
# solution 함수를 작성해 주세요.


#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(scores):
    size = len(scores)
    sscores = sorted(scores)
    print(sum(sscores), sscores[0], sscores[size-1],size)
    avg = int((sum(sscores) - sscores[0] - sscores[size-1] )/ size-2)
    print(avg)
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [90, 80, 70, 85, 100, 90]
ret = solution(scores)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

