from collections import defaultdict 

def solution(name, yearning, photo):
    answer = []
    dict = defaultdict(int)
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for li in photo:
        total = 0
        for e in li:
            total += dict[e] 
        answer.append(total)
        
    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name,yearning,photo))

