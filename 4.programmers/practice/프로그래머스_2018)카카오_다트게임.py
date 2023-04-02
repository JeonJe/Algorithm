

def solution(dartResult):
    answer = 0
    round_result = [ [0]*3 for _ in range(3) ]
    
    for i in range(3):
        round_result[i][2] = 1

    round = 0
    for idx, val in enumerate(dartResult):
        if val.isdigit():
            if int(val) == 0 and round_result[round][0] == 1:
                round_result[round][0] = 10
            else:
                round_result[round][0] = int(val)
        elif val.isalpha():
            if val == "S":
                round_result[round][1] = round_result[round][0]
            elif val == "D":
                round_result[round][1] = round_result[round][0]**(2)
            elif val == "T":
                round_result[round][1] = round_result[round][0]**(3)
            if idx+1<len(dartResult) and dartResult[idx+1].isalnum():
                round+=1
        else:
            if val == "*":
                if round == 0:
                    round_result[round][2] *= 2
                else:
                    round_result[round-1][2] *= 2
                    round_result[round][2] *= 2
            elif val == "#":
                round_result[round][2] *= -1
            round+=1
    
    print(round_result)
    for j in range(3):
        answer += round_result[j][1] * round_result[j][2]
    return answer

dartResult = "1T2D3D#"

print(solution(dartResult))