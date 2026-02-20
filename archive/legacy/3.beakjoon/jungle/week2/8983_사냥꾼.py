#사대의 수 M (1 ≤ M ≤ 100,000), 동물의 수 N (1 ≤ N ≤ 100,000), 사정거리 L (1 ≤ L ≤ 1,000,000,000)
import sys
M,N,L = map(int,sys.stdin.readline().split())
sadae = list(map(int,sys.stdin.readline().split()))
animal = [ list(map(int,sys.stdin.readline().split())) for _ in range(N) ]

sadae.sort()

cnt = 0

for a in animal:
    x = a[0]
    y = a[1]

    if y > L: continue
    
    left = 0
    right = len(sadae) - 1

    l_bound = x+y-L
    u_bound = x-y+L
    while left <= right:
        mid = (left + right) // 2
        if l_bound <= sadae[mid] <= u_bound:
            cnt+=1
            break
        if sadae[mid] < l_bound:
            left = mid + 1
        else:
            right = mid -1


print(cnt)