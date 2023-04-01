# from collections import defaultdict 
# import sys 
# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     n = int(input())
#     dict = defaultdict(int)
#     arr1 = list(map(int,input().split()))
#     for i in arr1:
#         dict[i] += 1


#     M = int(input())
#     arr2 = list(map(int,input().split()))
#     for j in arr2:
#         if dict[j] == 0:
#             print(0)
#         else:
#             print(1)
#!/bin/python3


#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


#
# Complete the 'maxLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#

       

def maxLength(a, k):
    answer = 0
    s = 0
    j = 0

    for i in range(len(a)):
        s += a[i]

        while s > k:
            s -= a[j]
            j += 1
            print(i,j,s)
        answer = max(answer, i-j+1)
    return answer



    

a = [1,2,3]
k = 4
result = maxLength(a, k)
print(result)

