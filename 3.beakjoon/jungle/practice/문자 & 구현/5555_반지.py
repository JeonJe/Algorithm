target = input()
n = int(input())

res = 0
for i in range(n):
    data = input()
    data *= 2
    data = list(data)
    for j in range(len(data)//2):
        if target == ''.join(data[j:j+len(target)]):
            res+=1
            break
print(res)