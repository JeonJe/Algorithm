from collections import defaultdict 

N, K = map(int,input().split())
seq = list(map(int,input().split()))

max_seq  = 0

# left, right 를 벌려가면서 조건 확인
left, right = 0, 0 
dict = defaultdict(int)

while left <= right and right < N:
  #조건을 만족하면 right 증가 
  if dict[seq[right]] < K:
      dict[seq[right]] += 1
      right += 1
  else:
     dict[seq[left]] -= 1
     left += 1
  max_seq = max(max_seq, right - left)    

print(max_seq)


