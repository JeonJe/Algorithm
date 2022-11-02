<<<<<<< HEAD
from random import randint
import time

array = []

for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] # swap

end_time = time.time()
print("선택 정렬 성능 측정 : ", end_time-start_time)

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

array.sort()

end_time =time.time()
=======
from random import randint
import time

array = []

for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] # swap

end_time = time.time()
print("선택 정렬 성능 측정 : ", end_time-start_time)

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

array.sort()

end_time =time.time()
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print("기본 정렬 라이브러리 성능 측정 :" ,end_time - start_time)