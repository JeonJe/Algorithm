

def solution(left, right):
    
    def check(n):
        res = []
        for j in range(1,n+1):
            if n % j == 0:
                res.append(j)
        return res 
    
    answer = 0
    for i in range(left,right+1):
        temp = check(i)
        
        if len(temp) % 2 == 0:
            answer += i
        else:
            answer -= i
    
        
    return answer