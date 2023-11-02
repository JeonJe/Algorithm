n = input()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

answer = 0
S = ""

for i in range(len(n)):
    # 현재 문자열 S에서 크로아티아 알파벳이 있는지 확인
    S += n[i]
    for a in alpha:
      if a in S:
          answer += 1
          S = S.replace(a, " ")   

list_S = list(S.split(" "))
for l in list_S:
  answer += len(l)
print(answer)