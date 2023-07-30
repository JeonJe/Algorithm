INF = 1e9
n = int(input())

graph = [[INF] * 52 for _ in range(52)]

def chr_to_ord(alp):
    if alp.isupper():
        return ord(alp) - ord("A")
    elif alp.islower():
        return ord(alp) - ord("a") + 26
    
def ord_to_chr(num):
    if num < 26:
        return chr(num + ord("A"))
    else:
        return chr(num + ord("a") - 26)
    
        
for i in range(1,52):
    for j in range(1,52):
        if i == j:
            graph[i][j] = 0

for _ in range(n):
    fr, to = input().split(" => ")
    ord_fr = chr_to_ord(fr)
    ord_to = chr_to_ord(to)
    graph[ord_fr][ord_to] = 1


for k in range(52):
    for i in range(52):
        for j in range(52):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

cnt = 0
answer = []
for i in range(52):
    for j in range(52):
        if i != j and graph[i][j] != INF:
          cnt += 1
          chr_i = ord_to_chr(i)
          chr_j = ord_to_chr(j)
          answer.append([chr_i, chr_j])

answer.sort()

print(cnt)
for ft, to in answer:
  print(f'{ft} => {to}')
