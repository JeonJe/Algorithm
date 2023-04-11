from collections import defaultdict 
from collections import deque

def solution(msg):
    answer = []
    dict = defaultdict(int)
    
    for i in range(0,26):
        dict[chr(65+i)] = i+1

                    
    queue = deque(msg)    
        
    w = queue.popleft()
    #큐가 빌 때 동안 확인 
    while queue:
        c = queue.popleft()
        wc = w+c
        #사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
        if wc in dict:
            w = wc
        else:
            #현재 입력의 사전 색인 번호 출력
            answer.append(dict[w])
            #사전에 등록
            dict[wc] = len(dict)+1
            #w 이동
            w = c
    answer.append(dict[w])
    
    return answer