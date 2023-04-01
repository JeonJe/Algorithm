#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getFinalString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getFinalString(s):
    # Write your code here
    target = "AWS"
    len_target = len(target)
    stack = []
    for e in s:
        stack.append(e)
        if e == target[-1] and target == "".join(stack[-len_target:]):
            del stack[-len_target:]
    print("".join(stack) if len(stack) > 0 else -1)
    return "".join(stack) if len(stack) > 0 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getFinalString(s)

    fptr.write(result + '\n')

    fptr.close()
