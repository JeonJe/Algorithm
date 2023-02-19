def solution(absolutes, signs):
    minus,plus = 0,0
    
    for i in range(len(signs)):
        if signs[i]:
            plus += absolutes[i]
        else:
            minus += absolutes[i]
        
    return plus - minus