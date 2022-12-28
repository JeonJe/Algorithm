K, N = map(int,input().split())

lan_cables = [ int(input()) for _ in range(K) ]
lan_cables.sort()

def check(mid):
    sum = 0
    for cable in lan_cables:
        sum += cable // mid
    if sum >= N:
        return True
    else:
        return False


left = 0
right = max(lan_cables)+1

while left + 1 < right:
    mid = (left + right) // 2

    if check(mid):
        left = mid 
    else:
        right = mid
print(left)


