N = int(input())

def find_sum_digit(N):
    s = 0 
    while N > 0:
        s += N % 10
        N = N // 10
    return s

res = 1e9
for i in range(1,N):
    sum_digit = find_sum_digit(i)
    if (i + sum_digit) == N:
        res = min(res, i)

print(res if res < 1e9 else 0)