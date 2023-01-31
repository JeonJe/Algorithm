from collections import defaultdict
trees = defaultdict(int)
total = 0
while True:
    try:
        tree = input()
        if tree == "":
            break
        total += 1
        trees[tree] += 1
    except:
        break

sorted_dict = sorted(trees.items())

for k,v in sorted_dict:
    print(f'{k} {(v/total)*100:.4f}')

