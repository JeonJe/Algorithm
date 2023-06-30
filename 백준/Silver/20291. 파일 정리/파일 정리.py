from collections import defaultdict 

n = int(input())

dict = defaultdict(int) 

for _ in range(n):
    target = input().split('.')[1]
    dict[target] += 1

sorted_dict = list(sorted(dict.items(), key=lambda x : x[0]))

for k, v in sorted_dict:
    print(k,v)

