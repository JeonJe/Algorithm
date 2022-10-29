
import sys

n = int(sys.stdin.readline())
counting_arry = [0] * (10001)

for _ in range(n):
    num = int(sys.stdin.readline())
    counting_arry[num] += 1

for i in range(len(counting_arry)):
    if counting_arry[i] != 0 :
    
        while counting_arry[i] > 0:
            print(i)
            counting_arry[i]-=1