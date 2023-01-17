n = int(input())


global res 
res = []

def make_seq(n,i):
    global res
    temp = []
    temp.append(n)
    temp.append(i)
    f = n
    s = i 
    while f - s >= 0:
        t = f - s
        temp.append(t)
        f = s
        s = t 
    
    if len(temp) > len(res):
        res = temp


for i in range(1,n+1):
    make_seq(n,i)

print(len(res))
print(*res)