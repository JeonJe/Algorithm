
import sys
from collections import deque
# sys.stdin = open("input.txt",'rt')

str1 = input()
str2 = input()

deq = deque(str2)

for x in str1:
    if x in deq:
        deq.remove(x)
    else:
        print("NO")
        break

else:
    if len(deq)==0:
        print("YES")
    else:
        print("NO")
        
        
    