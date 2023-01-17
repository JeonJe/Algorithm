def solution(X, Y):
    answer = ''
#     set_X = set(X)
#     set_Y = set(Y)
    
#     common = list(set_X & set_Y)
    
    
    for i in range(9,-1,-1):
        min_count = min(X.count(str(i)),Y.count(str(i)))
        answer += str(i) * min_count
    
    # answer = list(answer)
    if answer == '':
        return "-1" 
    if len(answer) == answer.count("0"):
        return "0"
    
    
    # answer = list(map(str,answer))
    
    return answer
