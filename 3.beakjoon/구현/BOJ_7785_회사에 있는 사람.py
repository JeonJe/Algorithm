from collections import defaultdict 
n = int(input())

dict = defaultdict(bool)
for i in range(n):
    name, status = input().split()
    if status == "enter":
        dict[name] = True
    else:
        dict[name] = False

temp = []
for idx, value in dict.items():
    if value:
        temp.append(idx)

temp.sort(reverse=True)
for name in temp:
    print(name)

    