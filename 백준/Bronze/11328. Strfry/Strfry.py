n = int(input())
for _ in range(n):
    fr, to = map(list,input().split())
    fr.sort()
    to.sort()
    print("Possible" if fr == to else "Impossible")