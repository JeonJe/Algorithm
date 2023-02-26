n = int(input())

folders = [ input() for _ in range(n) ]

ans = ''
for y in range(len(folders[0])):
    f = folders[0][y]
    match = True
    for x in range(1,n): 
        if folders[x][y] != f:
            match = False
    if match:
        ans += f
    else:
        ans += '?'
print(ans)
    
    