def solution(participant, completion):
    
    dict = { }
    for p in participant:
        if p not in dict:
            dict[p] = 1
        else:
            dict[p] += 1
            
    for c in completion:
        if dict[c] > 0:
            dict[c] -= 1
            if dict[c] == 0:
                dict.pop(c)
        else:
            return c
    
    key = dict.keys()
    for i in key:
        return i

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

print(solution(p,c))