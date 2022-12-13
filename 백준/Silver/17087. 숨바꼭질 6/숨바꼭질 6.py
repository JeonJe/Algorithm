
#수빈이 위치 s
n, s =map(int,input().split())
arr = list(map(int,input().split()))
diff = []

def gcd(x,y):
    if x < y:
        x,y = y,x
    if y == 0:
        return x
    return gcd(y, x%y)

for i in arr:
    diff.append(abs(s-i))

if len(diff) == 1:
    print(diff[0])
    exit()
elif len(diff) == 2:
    print(gcd(diff[0],diff[1]))
    exit()
else:
    temp = gcd(diff[0], diff[1])
    for j in range(2,len(diff)):
        temp = gcd(temp, diff[j])
    print(temp)
    exit()


    


