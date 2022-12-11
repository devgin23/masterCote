# [프로그래머스] 구명보트
from collections import deque
# 최대 2명만 탈 수 있다는 조건이 가장 중요!
# 그러면 무조건 2명을 태우는 게 좋으니까 가장 무거운 놈과 가장 가벼운 놈으로 2명 태우는게 젤 좋음.
def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)
    emptyDeque = deque([])
    while deq != emptyDeque:
        k = deq.pop()
        if deq == emptyDeque:
            answer += 1
            break
        else:
            if k + deque[0] <= limit:
                deq.popleft()
                answer += 1
            else:
                answer +=  1

    return answer

people = [40,40,50,60,70,120,130,140,240]

limit = 240
solution(people,limit)