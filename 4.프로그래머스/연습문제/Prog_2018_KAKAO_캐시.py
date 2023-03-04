from collections import deque 

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
    #cache hit 
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1

    #chace miss 
        else:

            if  len(cache) < cacheSize:
                cache.append(city)
            elif cacheSize > 0 :
                cache.popleft()
                cache.append(city)
            
            answer += 5

    return answer


cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))