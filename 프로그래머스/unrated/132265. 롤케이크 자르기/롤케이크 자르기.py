from collections import defaultdict 

def solution(topping):
    answer = 0
    num_of_topping = len(set(topping))
    brother = defaultdict(int)
    me = defaultdict(int)
        
    for t in topping:
        me[t] += 1
    
    for i in range(len(topping)):
        me[topping[i]] -= 1
        brother[topping[i]] += 1
        
        if me[topping[i]] == 0:
            del me[topping[i]]
        
        if len(me) == len(brother):
            answer += 1 

        
    return answer
