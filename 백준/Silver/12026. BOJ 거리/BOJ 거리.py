import sys

n = int(input())
street  = list(input())
dp = [sys.maxsize] * (n+1)
dp[0] = 0
#B는 J로부터와야하고, O는 B로부터와야하고, J는 O로부터 와야한다.
dict = {
    "B" : "J",
    "O" : "B",
    "J" : "O"
}

for i in range(len(street)):
    prev = dict[street[i]]
    for j in range(i):
        if street[j] == prev:
            dp[i] = min(dp[i], (i-j)**2 +dp[j])
print(dp[n-1] if dp[n-1] != sys.maxsize else -1)

