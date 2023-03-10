def solution(n, k):
    answer = 0
    
    cans = n // 10
    
    answer = 12000* n + (k-cans) * 2000
    return answer