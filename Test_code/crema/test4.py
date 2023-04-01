#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 


#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#
def longestChain(words):
    # Write your code here
    dict = defaultdict(int)
    words.sort(key=lambda x : len(x))
    
    for word in words:
        if len(word) > 1:
            dict[word] = 1
            for i in range(len(word)):
                temp = list(word[::])
                del temp[i]
                key = "".join(temp)
                if dict[key] > 0:
                    dict[word] = max(dict[key]+1, dict[word])
        else:
            dict[word] = 1
            
    sorted_dict = sorted(dict.items(), key=lambda x : -x[1])
    return sorted_dict[0][1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = longestChain(words)

    fptr.write(str(result) + '\n')

    fptr.close()
