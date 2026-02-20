import heapq 
n = int(input())
if n == 1:
    print(int(input()))
    exit(0)

nega = []
posi = []

for i in range(n):
    num = int(input())
    if num <= 0:
        nega.append(num)
    else:
        posi.append(num)

nega.sort()
posi.sort(reverse=True)

answer = 0
for i in range(0,len(nega),2):
    if i+1 < len(nega):
        answer += nega[i]*nega[i+1]
    else:
        answer += nega[i]
  
for i in range(0,len(posi),2):
    if i+1 < len(posi):
        if posi[i] != 1 and posi[i+1] != 1:
          answer += posi[i] * posi[i+1]
        else:
            answer += posi[i] + posi[i+1]
    else:
        answer += posi[i]

print(answer)
    




