h, w = map(int,input().split())
block = list(map(int,input().split()))

stack = []

if len(block) == 1:
    print(0)
    exit()

ans = 0
for i in range(len(block)):
    left_max = block[i]
    right_max = block[i]
    #왼쪽
    for a in range(i+1):
        left_max = max(left_max,block[a])
    #오른쪽
    for b in range(i,len(block)):
        right_max = max(right_max,block[b])
    
    min_height = min(left_max,right_max)

    ans += min_height - block[i]

print(ans)
