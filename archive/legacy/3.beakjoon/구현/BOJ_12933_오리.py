from collections import defaultdict

seq = input()
dict = defaultdict(int)

sound = 'quack'
position = defaultdict(int)

for i in range(len(sound)):
    position[sound[i]] = i

answer = 0
for i in range(len(seq)):

    current = seq[i]
    dict[current] += 1
    
    if current == sound[0]:
        answer = max(answer, dict[sound[0]])

    if position[current] > 0:
        cur_idx = position[current]
        prev_idx = position[current] - 1
        if dict[sound[prev_idx]] < dict[sound[cur_idx]]:
            print(-1)
            exit(0)

    if seq[i] == sound[-1]:
        for i in range(len(sound)):
            dict[sound[i]] -= 1

for i in range(len(sound)):
    if dict[sound[i]] != 0:
        print(-1)
        exit(0)
    
print(answer)



