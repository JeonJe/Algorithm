def solution(s):
    answer = [0,0]
    
    while s != "1" :
        remove_zero_s = ''  
        answer[0] += 1
        for elem in s:
            if elem == "1":
                remove_zero_s += '1'
            else:
                answer[1] += 1
        c = len(remove_zero_s)
        s = bin(c)[2:]
        
    return answer
