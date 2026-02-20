<<<<<<< HEAD
N,M,K = map(int,input().split())

arr = list(map(int,input().split()))
print(arr)

sorted_array = sorted(arr,reverse=True)

f = sorted_array[0]
s = sorted_array[1]

result = 0

count = int(M/(K+1)) * K # M/(K+1)은 순서가 반복되는 횟수, K는 가장 큰수가 반복되는 순서에서 나타나는 횟수
count += M % (K+1) # 반복되는 사이클을 마치고, 나머지에서 가장 큰수가 나타나는 횟수


result += count*f # 가장큰수 * 가장큰수가 나타나는 횟수
result += (M-count)*s  # 전체 횟수 - 가장 큰수가 나타내는 횟수 * 두번째로 큰수

=======
N,M,K = map(int,input().split())

arr = list(map(int,input().split()))
print(arr)

sorted_array = sorted(arr,reverse=True)

f = sorted_array[0]
s = sorted_array[1]

result = 0

count = int(M/(K+1)) * K # M/(K+1)은 순서가 반복되는 횟수, K는 가장 큰수가 반복되는 순서에서 나타나는 횟수
count += M % (K+1) # 반복되는 사이클을 마치고, 나머지에서 가장 큰수가 나타나는 횟수


result += count*f # 가장큰수 * 가장큰수가 나타나는 횟수
result += (M-count)*s  # 전체 횟수 - 가장 큰수가 나타내는 횟수 * 두번째로 큰수

>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(result)