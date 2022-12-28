# [프로그래머스] [1차]캐시
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(['']*cacheSize)
    if cacheSize < 1 :
        return 5*len(cities)
    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            #LRU(Least Recently Used)
            cache.remove(i)
            cache.append(i)
        else:
            answer += 5
            cache.popleft()
            cache.append(i)
    print(answer)
    return answer        
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Seoul", "NewYork", "Rome"]
cacheSize = 5
solution(cacheSize, cities)