n, t = map(int,input().split())

seq = []
left, right = 0, 0
total_Ri, total_Li = 0, 0

def check(seq, S, T):
    total_min, total_max = 0, 0
    
    for Li, Ri in seq:
      if Li > S:
          return False      
      total_min += Li
      total_max += min(Ri, S)

    return total_min <= T <= total_max

for i in range(n):
    Li, Ri = map(int,input().split())
    total_Ri += Ri
    total_Li += Li
    seq.append([Li, Ri])
    right = max(right, Ri)
  
if total_Li > t or total_Ri < t:
    print(-1)
    exit()

while left + 1< right:
    mid = (left + right) // 2
    if check(seq, mid, t):
        right = mid
    else:
        left = mid
print(right)

