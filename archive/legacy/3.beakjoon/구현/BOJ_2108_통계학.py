from collections import Counter

n = int(input())
seq = list(int(input()) for _ in range(n))

seq.sort()

average = round(sum(seq) / len(seq))
print(average)

median = seq[(len(seq))//2-1] if n % 2 == 0 else seq[len(seq)//2]
print(median)

count = list(Counter(seq).most_common())
max_freq = count[0][1]

same_freq = []
for num, freq in count:
  if freq == max_freq:
    same_freq.append(num)
  else:
    break
same_freq.sort()

mode = same_freq[0] if len(same_freq) == 1 else same_freq[1]
print(mode)

range = seq[-1] - seq[0]
print(range)
