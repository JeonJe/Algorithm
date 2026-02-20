t = int(input())

for _ in range(t):
  n = int(input())
  first_row = list(map(int,input()))
  second_row = list(input())
  answer = 0 
  for i in range(n):
    if i == 0:
      if first_row[i] != 0 and first_row[i+1] != 0:
        first_row[i] -= 1
        first_row[i+1] -= 1
        answer += 1
    elif i == n-1:
      if first_row[i] != 0 and first_row[i-1] != 0:
        first_row[i] -= 1
        first_row[i-1] -= 1
        answer += 1
    else:
      if first_row[i] != 0 and first_row[i-1] != 0 and first_row[i+1] != 0:
        first_row[i] -= 1
        first_row[i-1] -= 1
        first_row[i+1] -= 1
        answer += 1
  print(answer)




