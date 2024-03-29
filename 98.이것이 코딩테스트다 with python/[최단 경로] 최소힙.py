<<<<<<< HEAD
import heapq

def heapsort(iterable):
    h = []
    result = []

    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
        #최대힙의 경우 heapq.heappush(h,-value)

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append((heapq.heappop(h)))
        #최대힙의 경우 result.append((-heapq.heappop(h))

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,10])

print(result)

=======
import heapq

def heapsort(iterable):
    h = []
    result = []

    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
        #최대힙의 경우 heapq.heappush(h,-value)

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append((heapq.heappop(h)))
        #최대힙의 경우 result.append((-heapq.heappop(h))

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,10])

print(result)

>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
