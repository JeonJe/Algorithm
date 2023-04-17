
from collections import defaultdict
n = list(input())
answer = 0
dict = defaultdict(int)

for i in range(len(n)):
    if n[i] == "6" or n[i] == "9":
        if dict["6"] <= dict["9"]:
            dict["6"] += 1
        else:
            dict["9"] += 1
    else:
        dict[n[i]] += 1



sorted_dict = sorted(dict.items(), key=lambda x : -x[1])
print(sorted_dict[0][1])
    


