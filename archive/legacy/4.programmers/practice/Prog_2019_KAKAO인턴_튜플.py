
from collections import defaultdict 

def solution(s):
    answer = []
    dict = defaultdict(int)
    s = map(int,(s.replace("{","").replace("}","")).split(","))
    for num in s:
        dict[num] += 1
    
    sorted_dict = sorted(dict.items(), key = lambda x : x[1], reverse=True)
    for a,_ in sorted_dict:
        answer.append(a)

    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))