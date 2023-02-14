from collections import defaultdict 

def solution(k, tangerine):
    answer = 0
    
    box = defaultdict(int)
    for t in tangerine:
        box[t] += 1
    
    box = sorted(box.items(), key=lambda item : item[1] , reverse=True)

    for _, v in box:
        if k > 0:
            k -= v 
            answer+=1
        else:
            break

    return answer