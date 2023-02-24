
def solution(n,a,b):
    def matching(a,b):
        if a % 2 == 0:
            return False
        else:
            if a+1 == b:
                return True
            return False
    
    answer = 0

    left = min(a,b)
    right = max(a,b)
    
    while not matching(left,right):
        if left % 2 == 0:
            left = left // 2
        else:
            left = left // 2 + 1
        if right % 2 == 0:
            right = right // 2
        else:
            right = right // 2 + 1
            
        answer+=1
            
    return answer+1