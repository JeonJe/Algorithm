from collections import defaultdict

dict = defaultdict()

def solution(s):
    s = list(s)
    res = []
    for i in range(len(s)):
        #현재 확인 중인 문자
        cur = s[i]
        #나온적이 없는 문자이면, res에 -1
        
        if cur not in dict:
            res.append(-1)
        #현재 문자의 인덱스 저장
            dict[cur] = i
        else:
        #ㅇ
            res.append(i - dict[cur])
            dict[cur] = i
    return res 


