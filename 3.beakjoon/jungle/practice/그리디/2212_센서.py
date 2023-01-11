N = int(input())
K = int(input())

sensors = list(map(int,input().split()))
sensors.sort()

diff = []
for i in range(1,len(sensors)):
    diff.append(sensors[i] - sensors[i-1])

diff.sort(reverse=True)
print(sum(diff[K-1:]))


