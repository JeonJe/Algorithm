from collections import defaultdict 
from copy import copy

def solution(want, number, discount):
    dict = defaultdict(int)
    answer = 0

    for i in range(len(want)):
        dict[want[i]] = number[i]
    
    for i in range(len(discount)-10+1):
        temp = copy(dict)
        
        for j in range(i,i+10):
            temp[discount[j]] -= 1
        
        isAnswer = True
        for _, value in temp.items():
            if value != 0:
                isAnswer = False
                break
        
        if isAnswer:
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want,number,discount))
