from collections import defaultdict 

while True:
  N, M = map(int,input().split())
  if N == 0 and M == 0:
    break

  dict = defaultdict(int)
  for i in range(N):
    ranks = list(map(int,input().split()))

    for ranker in ranks:
      dict[ranker] += 1
      

  sorted_dict = sorted(dict.items(), key = lambda x : (-x[1],x[0]))
  second_max = sorted_dict[1][1]

  answer = []
  for key, value in sorted_dict:
    if value == second_max:
      answer.append(key)
    elif value < second_max:
      break

  print(*answer)