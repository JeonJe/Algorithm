
import sys
from collections import defaultdict


# sys.stdin = open("input.txt",'rt')

n= int(input())
arr = list(map(int,input().split()))

m = int(input())
target = list(map(int,input().split()))

dict = defaultdict()
for i in arr:
    try: dict[i] += 1
    except: dict[i]=1

for i in target:
    if i in dict:
        print(dict[i],end=' ')
    else:
        print(0,end=' ')
    
    
