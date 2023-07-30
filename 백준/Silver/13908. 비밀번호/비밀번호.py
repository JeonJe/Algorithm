
n, m = map(int,input().split())

if m > 0:
  seq = list(map(int,input().split()))
else:
  seq = []

cnt = 0
def dfs(depth, path):
  if len(path) >= n:
    candi = True
    for num in seq:
      if num not in path:
        candi = False
        break
    if candi:
      global cnt
      cnt+=1

    return 
  
  for i in range(0,10):
      path.append(i)
      dfs(depth+1, path)
      path.pop()

dfs(0,[])
print(cnt)