# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)
    arr = [0] * (n+2)

    for a in A:
        arr[a] = 1
    
    for i in range(1,n+2):
        if arr[i] == 0:
            return i
    

    
