N, L, W, H = map(int, input().split())

left = 0
right = max(L,W,H)

def check(N, L, W, H, mid):
    if (L // mid) * (W // mid) * (H // mid) >= N:
        return True
    else:
        return False
    

for _ in range(10000):
# while left+1 < right:
    mid = (left + right) / 2

    if check(N,L, W, H,mid):
        left = mid
    else:
        right = mid

print(f'{left:.9f}')