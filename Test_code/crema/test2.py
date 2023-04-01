
import math
import os
import random
import re
import sys


#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#

def findRange(num):
    # Write your code here
    min_value = sys.maxsize
    max_value = -sys.maxsize
    n = str(num)
    for i in range(len(n)):
        for j in range(10):
            temp = n[::]
            temp = temp.replace(temp[i],str(j))
            max_value = max(max_value, int(temp))
            if temp[0] != "0":
                min_value = min(min_value, int(temp))
            
    print(max_value, min_value)
    return int(max_value - min_value)
    


    
if __name__ == '__main__':
    n = 909

    result = findRange(n)

    print(result)
