def solution(numbers):
    answer = 0
    tot = 0
    for n in numbers:
        tot += n
    
    return tot / len(numbers)