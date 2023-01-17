from collections import defaultdict

def solution(survey, choices):
    answer = ''
    Character = defaultdict(int)

    for i in range(len(choices)):
        if choices[i] == 1:
            Character[survey[i][0]]+=3
        elif choices[i] == 2:
            Character[survey[i][0]]+=2
        elif choices[i] == 3:
            Character[survey[i][0]]+=1
        elif choices[i] == 5:
            Character[survey[i][1]]+=1
        elif choices[i] == 6:
            Character[survey[i][1]]+=2
        elif choices[i] == 7:
            Character[survey[i][1]]+=3
    
    if Character["R"] >= Character["T"]:
        answer+='R'
    else:
        answer+='T'
    if Character["C"] >= Character["F"]:
        answer+='C'
    else:
        answer+='F'
    if Character["J"] >= Character["M"]:
        answer+='J'
    else:
        answer+='M'
    if Character["A"] >= Character["N"]:
        answer+='A'
    else:
        answer+='N'

        

    return answer



survey = ["TR", "RT", "TR"]
choices = 	[7, 1, 3]

print(solution(survey,choices))