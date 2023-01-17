
arr = [int(input())for _ in range(10)]

res = set()

for i in arr:
    res.add(i%42)

print(len(res))