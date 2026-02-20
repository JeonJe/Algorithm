<<<<<<< HEAD
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1]+d[i-2]*2) %796796

=======
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1]+d[i-2]*2) %796796

>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(d[n])