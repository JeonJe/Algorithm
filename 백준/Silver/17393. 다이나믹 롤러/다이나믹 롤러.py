N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


def upper_bound(seq, target):
    left = 0
    right = len(seq)

    while left < right:
        mid = (left + right) // 2

        if seq[mid] <= target:
            left = mid + 1
        else:
            right = mid 
    return right 

answer = []
for i in range(N):
    idx = upper_bound(B, A[i])
    answer.append(idx - i - 1)
print(*answer)
    