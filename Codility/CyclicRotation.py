# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    length = len(A)
    arr = [0]*length
    for i in range(length):
        arr[(i+K)%length] = A[i]
    return arr

A = [3, 8, 9, 7, 6]
K = 2
print(solution(A,K))