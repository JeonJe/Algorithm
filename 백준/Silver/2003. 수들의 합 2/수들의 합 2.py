n, m = map(int, input().split())
seq = list(map(int,input().split()))

answer = 0

left, right = 0, 0
cur_sum = seq[left]

while left < n and right < n:
    if cur_sum == m:
      answer+=1
      right += 1
      if right == n:
         break 
      cur_sum += seq[right]
    elif cur_sum < m:
      right += 1
      if right == n:
         break
      cur_sum += seq[right]
      
    else:
      cur_sum -= seq[left]
      left += 1
print(answer)