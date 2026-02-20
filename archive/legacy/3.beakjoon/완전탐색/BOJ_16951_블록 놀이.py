import copy
N, K = map(int,input().split())
origin_seq = list(map(int,input().split()))

def how_many_change(i):
    seq = copy.deepcopy(origin_seq)
    left, right = i-1, i+1
    left_cnt, right_cnt = 0, 0
    while left >= 0:
        if seq[left] != seq[left+1] - K:
            left_cnt += 1
            seq[left] = seq[left+1] - K
            if seq[left] < 1:
                return N
        left -= 1
    
    while right < N:
        if seq[right] != seq[right-1] + K :
            right_cnt += 1
            seq[right] = seq[right-1] + K
            if seq[right] < 1:
                return N
        right += 1

    return left_cnt + right_cnt
            
answer = N
for i in range(N):
    result = how_many_change(i)
    answer = min(answer, result)

print(answer)
