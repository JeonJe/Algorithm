import sys
n,m = map(int,input().split())

seq = [int(input()) for _ in range(n)]


seq.sort()
left, right = 0, 0
answer = max(seq) - min(seq)

while left <= right and right < n:

    if seq[right] - seq[left] < m:
        right += 1

    else:
        answer = min(answer, seq[right]-seq[left])
        left += 1
        

print(answer)
