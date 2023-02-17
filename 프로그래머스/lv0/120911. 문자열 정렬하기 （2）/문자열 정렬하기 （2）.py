def solution(my_string):
    answer = ''
    answer = my_string.lower()
    answer = list(answer)
    answer.sort()
    return ''.join(answer)