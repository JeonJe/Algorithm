 
 
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    dict = defaultdict(int)

    for i in range(len(A)):
        dict[A[i]] += 1 

    for key,value in dict.items():
        if value % 2 != 0:
            return key 

A = [9, 3, 9, 3, 9, 7, 9]

print(solution((A)))