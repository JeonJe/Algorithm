from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    #course 가 2,3,5 라면 2개짜리 단품조합,3개짜리 단품조합, 5개짜리 단품조합
    for c in course:
        temp = []
        #각 손님들이 주문한 단품메뉴들을 확인
        for order in orders:
            #ABC 조합은 BCA 조합과 동일하므로 sorted 로 정렬하여 똑같이 맞춰주고
            #손님들의 order에 대한 C개의 단품 조합의 경우를 com에 입력
            comb = combinations(sorted(order), c)

            #2,3,5개짜리 단품조합의 경우를 temp에 모두 담음
            temp += comb
            
        #딕셔너리 형태로 각 알파벳이 몇번나왔는지 카운팅
        # print(list(temp))
        counter = Counter(temp) 
        
        # len(counter)가 0이면 해당 주문 조합이 나온적이 없는 것. ->패스 
        #max(counter.value()) == 1 이면 해당 조합 주문을 혼자한 것. -> 패스
        
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
            
            
    return sorted(answer)