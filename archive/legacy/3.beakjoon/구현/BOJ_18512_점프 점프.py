x,y,p1,p2 = map(int,input().split())

p1_list, p2_list = [], []

while p1 <= 10000:
    p1_list.append(p1)
    p1 += x
    
while p2 <= 10000:
    if p2 in p1_list:
        print(p2)
        exit(0)
        
    p2 += y
print(-1)
       
        