from collections import defaultdict

seq = input()
dict = defaultdict(int)

sound = ['q','u','a','c','k']
answer = 0

for i in range(len(seq)):
    dict[seq[i]] += 1
    if seq[i] == sound[0]:
        answer = max(answer, dict[sound[0]])

    for j in range(1,len(sound)):
        if dict[sound[j-1]]< dict[sound[j]]:
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



