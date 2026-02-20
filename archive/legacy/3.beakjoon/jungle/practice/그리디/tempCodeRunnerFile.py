N, K= map(int,input())

t = list(map(int,input().split()))
t.sort()

diff = []
for i in range(1,len(t)):
    diff.append(t[i] - t[i-1])

diff.sort(reverse=True)
print(sum(diff[K-1:]))


