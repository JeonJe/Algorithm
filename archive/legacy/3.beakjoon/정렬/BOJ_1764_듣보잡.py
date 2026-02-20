
import sys 
from collections import defaultdict

n,m = map(int,input().split())
dict = defaultdict(int)

for i in range(n):
    h = input()
    dict[h] += 1

for j in range(m):
    h2 = input()
    dict[h2] += 1

answer = []
for key,value in dict.items():
    if value == 2:
        answer.append(key)

answer.sort()
print(len(answer))
for a in answer:
    print(a)


