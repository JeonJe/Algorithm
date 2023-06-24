t = int(input())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

for _ in range(t):
    seq = list(map(int,input().split()))
    n = seq[0]
    nums = seq[1:]

    total = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            total += gcd(nums[i], nums[j])
            
    print(total)

