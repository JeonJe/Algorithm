def solution(n, m, section):
    
    def check(mid):
        last = 0
        cnt = 0
        for sect in section:                
            if sect > last:
                cnt += 1
                last = sect+m-1
                
        return True if cnt <= mid else False
            
    left, right = 0, n+1
    
    while left+1 < right:
        mid = (left+right) // 2
        
        if not check(mid):
            left = mid
        else:
            right = mid
    
    return right