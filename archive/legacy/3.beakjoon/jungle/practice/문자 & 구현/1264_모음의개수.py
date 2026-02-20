
res = 0

target = ['a','e','i','o','u']

while True:
    sentence = input().lower()
    
    if sentence == '#':
        break
    res = 0
    for t in target:
        res += sentence.count(t)
    print(res)