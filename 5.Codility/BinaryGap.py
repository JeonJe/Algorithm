def solution(N):
    # Implement your solution here
    binary = list(bin(N)[2:])
    idx = 1
    longest_gap = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            gap = i-idx-1
            idx = i
            longest_gap = max(longest_gap,gap)
    return longest_gap

N=529
print(solution(N))
