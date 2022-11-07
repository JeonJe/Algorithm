#사대의 수 M (1 ≤ M ≤ 100,000), 동물의 수 N (1 ≤ N ≤ 100,000), 사정거리 L (1 ≤ L ≤ 1,000,000,000)
import sys
M,N,L = map(int,sys.stdin.readline().split())
sadae = list(map(int,sys.stdin.readline().split()))
animal = [ list(map(int,sys.stdin.readline().split())) for _ in range(N) ]

sadae.sort()
# animal.sort(key= lambda x : x[0])
cnt = 0
for a in animal:
    x = a[0]
    y = a[1]

    if y > x+L: continue

    l_bound = x+y-L
    u_bound = x-y+L
    left =0
    right = len(sadae) -1
    while left <= right:
        mid = (left+right) // 2

        if l_bound <= sadae[mid] <= u_bound:
            cnt += 1
            break
        elif l_bound > sadae[mid]:
            left = mid + 1
        elif sadae[mid] > u_bound:
            right = mid - 1

print(cnt)