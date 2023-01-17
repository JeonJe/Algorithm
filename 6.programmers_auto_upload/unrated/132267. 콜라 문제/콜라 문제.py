def solution(a, b, n):
    answer = 0
    while n // a > 0:
        m = n // a
        answer += m*b
        n = n % a + m*b
    return answer