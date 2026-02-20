
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    num_B = S.count("B")
    num_A = S.count("A")
    num_N = S.count("N")

    #B는 1개, A는 3개, N은 2개로 구성
    cnt = 0
    b =  num_B // 1
    a = num_A // 3
    n = num_N // 2
    cnt = min(b,a,n)

    return cnt


S = "NAANAAXNABABYNNBZ"
print(solution(S))