from collections import defaultdict

n, m = map(int, input().split())
info = defaultdict(list)

for _ in range(m):
    ice_number, dont_mix = map(int, input().split())
    info[ice_number-1].append(dont_mix-1)

answer = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n): 
            if k not in info[j] and k not in info[i]:
                if j not in info[i] and j not in info[k]:
                    if i not in info[k] and i not in info[j]:
                        answer += 1

print(answer)