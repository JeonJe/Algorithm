
#
# #문제7
# 오름차순으로 정렬되어있는 두 리스트 arrA, arrB를 하나의 리스트로 합치려 합니다. 단, 합친 후의 리스트도 오름차순으로 정렬되어 있어야 합니다.
#
# 예를 들어 arrA = [-2, 3, 5, 9], arrB = [0, 1, 5]인 경우 두 리스트을 오름차순으로 정렬된 하나의 리스트로 합치면 [-2, 0, 1, 3, 5, 5, 9]가 됩니다.
#
# 오름차순으로 정렬된 두 리스트 arrA와 arrB가 주어졌을 때, 두 리스트를 오름차순으로 정렬된 하나의 리스트로 합쳐서 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.
#
# ---
# ##### 매개변수 설명
# 오름차순으로 정렬된 두 리스트 arrA와 arrB가 solution 함수의 매개변수로 주어집니다.
#
# * arrA의 길이는 1 이상 200,000 이하입니다.
# * arrA의 원소는 -1,000,000 이상 1,000,000 이하의 정수입니다.
# * arrB의 길이는 1 이상 200,000 이하입니다.
# * arrB의 원소는 -1,000,000 이상 1,000,000 이하의 정수입니다.
#
# ---
# ##### return 값 설명
# 두 리스트 arrA, arrB를 오름차순으로 정렬된 하나의 리스트로 합쳐서 return 해주세요.
#
# ---
# ##### 예시
#
# | arrA          | arrB      | return                 |
# |---------------|-----------|------------------------|
# | [-2, 3, 5, 9] | [0, 1, 5] | [-2, 0, 1, 3, 5, 5, 9] |



def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA)
    arrB_len = len(arrB)
    answer = []
    while arrA_idx < arrA_len and arrB_idx < arrB_len:
        if arrA[arrA_idx] < arrB[arrB_idx]: #두개 비교해가며
            answer.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            answer.append(arrB[arrB_idx])
            arrB_idx += 1

    while arrA_idx<arrA_len:  # 한 쪽 배열이 다 채워졌을 경우
        answer.append(arrA[arrA_idx])
        arrA_idx += 1
    while arrB_idx<arrB_len:
        answer.append(arrB[arrB_idx])
        arrB_idx += 1
    return answer


#The following is code to output testcase.
arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")