T = int(input())

for _ in range(T):

    H,W,N = map(int,input().split())

    if N % H != 0:
        x = str((N//H)+1).zfill(2)
        y = str(N%H)
    else:
        x = str((N//H)).zfill(2)
        y = str(H)

    print(y+x)
