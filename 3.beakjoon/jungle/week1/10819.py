import itertools

def cal(permutation):

    s = 0
    for i in range(len(permutation)-1):
        s += abs(permutation[i] - permutation[i+1])
    return s

n = int(input())
arr =  list(map(int,input().split()))
permutations = list(itertools.permutations(arr, len(arr)))
max_sum = 0

for permutation in permutations:
    
    s = cal(permutation)
    max_sum = max(max_sum, s)

print(max_sum)