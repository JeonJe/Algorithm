import sys
X,Y = input().split()

res = 0
if len(X) == len(Y):
    for i in range(len(X)):
        if X[i] != Y[i]:
            res +=1
    print(res)
    exit()

res = sys.maxsize
for i in range(len(Y)-len(X)+1):
    cnt = 0
    for j in range(len(X)):
        if X[j] != Y[i+j]:
            cnt+=1
    res = min(res,cnt)

print(res)
            
