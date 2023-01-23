from collections import defaultdict

n = int(input())
postfix = input()
nums = defaultdict(int)
for i in range(n):
    v = int(input())
    nums[chr(65+i)] = v

stack = []
for idx, p in enumerate(postfix):
    
    if p.isalpha():
        stack.append(nums[p])
    else:
        s = stack.pop()
        f = stack.pop()
        stack.append(eval(str(f)+p+str(s)))

print(f'{stack.pop():.2f}')