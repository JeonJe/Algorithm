s, k = map(int,input().split())

d = s // k 
m = s % k 

temp = [d] * k 

for i in range(m):
    temp[i]+=1

ans = 1

for i in temp:
    ans *= i
print(ans)