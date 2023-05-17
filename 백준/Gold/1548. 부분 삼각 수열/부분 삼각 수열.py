n = int(input())
seq = list(map(int,input().split()))

seq.sort()
if n <= 2:
    answer = n 
else:
    answer = -1
    for i in range(0,n-2):    
        for k in range(n-1,i+1,-1):
            if seq[i] + seq[i+1] > seq[k]:
                answer = max(answer, k - i + 1)
                break

    if answer == -1:
        answer = 2

print(answer)
