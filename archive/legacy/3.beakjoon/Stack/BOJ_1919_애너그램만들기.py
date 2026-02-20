from collections import defaultdict

a = input()
b = input() 
dict = defaultdict(int)

for ch in a:
    dict[ch] += 1
for ch in b:
    dict[ch] -= 1

answer = 0
for _,value in dict.items():
    answer += abs(value)
print(answer)