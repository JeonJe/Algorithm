n, s = map(int, input().split())
arr = list(map(int, input().split()))


def func(idx, d):
    global cnt
    if (idx == n):
        if (s == d):
            cnt += 1
            return
    else:
        func(idx + 1, d + arr[idx])
        func(idx + 1, d)

cnt = 0
func(0, 0)

if (s == 0):
    cnt -= 1
print(cnt)