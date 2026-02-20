<<<<<<< HEAD
N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1


=======
N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1


>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(count)