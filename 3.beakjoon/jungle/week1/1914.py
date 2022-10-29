# n = 3
n = int(input())

def move (b, start, end):
        print(f"{start} {end}")


def hanoi(n, start, end, sub):

    if n == 1:
        move(1,start,end)
    else:
        hanoi(n-1, start, sub, end)
        move(n, start,end)
        hanoi(n-1, sub, end, start)

print((2**n)-1)
if n <= 20:
    hanoi(n,1,3,2)