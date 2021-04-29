N = list(str(input()))


mid = int(len(N)//2)
sumA,sumB = 0,0
for i in range(mid):
    sumA+=int(N[i])

for j in range(mid,len(N)):
    sumB+=int(N[j])

if sumA==sumB:
    print("Lucky")
else:
    print("Ready")