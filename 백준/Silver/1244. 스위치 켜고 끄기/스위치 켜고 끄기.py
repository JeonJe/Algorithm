import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
seq.insert(0, -1)
m = int(input())

def man(target):
  for i in range(target, len(seq),target):
    seq[i] = seq[i] ^ 1


def woman(target):
  left, right = target-1, target+1
  seq[target] = seq[target] ^ 1

  while left > 0 and right < len(seq):
    if seq[left] == seq[right]:
      seq[left] = seq[left] ^ 1
      seq[right] = seq[right] ^ 1
      left -= 1
      right += 1
    else:
      break


for i in range(m):
  gender, target = map(int, input().split())

  if gender == 1:
    #남자 
    man(target)
  else:
    #여자
    woman(target)

for i in range(1,len(seq)):
  print(seq[i], end=' ')
  if i % 20 == 0:
    print()