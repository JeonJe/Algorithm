from collections import defaultdict 

def solution(name, yearning, photo):
    answer = []
    dict = defaultdict(int)
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for li in photo:
        total = 0
        for e in li:
            total += dict[e] 
        answer.append(total)
        
    return answer
