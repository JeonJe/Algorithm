def solution(s):
    answer = 0
    num_list = list(s.split())
    last = 0
    for n in num_list:
        if n ==  "Z":
            answer -= last
        else:
            last = int(n)
            answer += last
            
    return answer