n = int(input())
candidates = [list(map(int,input().split())) for _ in range(n)]

def check(target):

  for num, s, b in candidates:
      list_num = [int(digit) for digit in str(num) ]
      check_s, check_b = 0, 0

      for idx, value in enumerate(list_num):
          if value == target[idx]:
              check_s += 1
          else:
              if target[idx] in list_num:
                check_b += 1

      if check_s != s or check_b != b:
          return False

  return True 
  
def dfs(depth, path):
    if len(path) >= 3:
        if check(path):
            global answer 
            answer += 1
        return 

    for i in range(1,10):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs(depth+1, path)
            path.pop()
            visited[i] = False
answer = 0
visited = [False]*10
dfs(0,[])
print(answer)