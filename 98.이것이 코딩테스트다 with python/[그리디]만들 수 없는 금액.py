<<<<<<< HEAD
N = int(input())

data = list(map(int,input().split()))

#최솟값을 증가하면서 확인하느냐


data.sort()

target = 1

for x in data:
    print(target, x )
    if target < x:
        break
    target+=x

=======
N = int(input())

data = list(map(int,input().split()))

#최솟값을 증가하면서 확인하느냐


data.sort()

target = 1

for x in data:
    print(target, x )
    if target < x:
        break
    target+=x

>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(target)