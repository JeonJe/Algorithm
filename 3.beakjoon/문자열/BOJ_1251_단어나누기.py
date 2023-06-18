seq = input()

answer = []
n = len(seq)
for i in range(0,n):
    for j in range(i,n):
        left = seq[:i]
        mid = seq[i:j+1]
        right = seq[j+1:]
        if len(left) == 0 or len(mid) == 0 or len(right) == 0:
            continue
        reversed_left = list(reversed(left))
        reversed_mid = list(reversed(mid))
        reversed_right = list(reversed(right))
        answer.append("".join(reversed_left + reversed_mid + reversed_right))

answer.sort()
print(answer[0])
