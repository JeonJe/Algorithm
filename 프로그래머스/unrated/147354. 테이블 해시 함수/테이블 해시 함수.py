
def solution(data,col,row_begin,row_end):
    answer = 0
    S_i = []
    #테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되,
    #만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬합니다.
    data.sort(key=lambda x : (x[col-1], -x[0]))
    # 정렬된 데이터에서 S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의합니다.
    for i in range(len(data)):
        s = 0
        for j in range(len(data[0])):
            s += data[i][j] % (i+1)
        S_i.append(s)
    # row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환합니다.
    answer = S_i[row_begin-1]
    for i in range(row_begin, row_end):
        answer = answer ^ S_i[i]


    return answer 