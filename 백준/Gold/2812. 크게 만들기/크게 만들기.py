N, K = map(int,input().split())

n = list(map(int,input()))
stack = []

remove_cnt = 0
for i in range(N):  

  while stack and stack[-1] < n[i]:
    stack.pop()
    remove_cnt += 1

    if remove_cnt == K:
      print("".join(map(str,stack)) + str(n[i]) + "".join(map(str,n[i+1:])))
      exit(0)
  stack.append(int(n[i]))

print("".join(map(str, stack[:-(K-remove_cnt)])))