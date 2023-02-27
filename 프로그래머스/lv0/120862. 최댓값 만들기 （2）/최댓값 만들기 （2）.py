def solution(numbers):
    answer = 0
    negative = []
    positive = []
    for i in numbers:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    negative.sort()
    positive.sort()
    
    max_positive, max_negative, mix = -1e9, -1e9, -1e9
    if len(positive) == 1 and len(negative) == 1:
        mix = positive[-1] * negative[0]
    if len(positive) >= 2:
        max_positive = positive[-1] * positive[-2]
    if len(negative) >= 2:
        max_negative = negative[0] * negative[1]
    
    
    answer = max(max_positive, max_negative, mix)
            
    
    return answer