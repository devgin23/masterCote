# [프로그래머스] 구명보트
from collections import deque
def solution(people, limit):
    answer = 0
    # 가장 큰 놈을 먼저 넣는다.
    # 그 다음부터는 넣을 수 있는 놈 중 가장 큰놈을 넣는다.
    people.sort(reverse=True)
    que = (people)
    print(people)
    inBoat = []
    weight = 0
    while que != []:
        # 남은 놈들 curQue에 넣는다.
        curQue = list(que)
        # 2명만 탈 수 있다는 조건 나중에 봄.
        if len(inBoat)==2:
            answer += 1
            inBoat = []
            weight = 0
        for i in range(len(curQue)):
            flagAdd = False
            # 큰 놈 부터 본다.
            # 들어갈 수 있으면 넣고 break
            # 끝까지 봤는데 넣을 수 없으면 보트 출발.
            if weight + curQue[i] <= limit:
                # 들어갈 수 있으면 넣고 que에서 빼주고
                inBoat.append(curQue[i])
                weight += curQue[i]
                que.remove(curQue[i])
                flagAdd = True
                break
        if not flagAdd:
            answer += 1
            inBoat = []
            weight = 0
    print(answer + 1)
    return answer + 1


people = [40,40,50,60,70,120,130,140,240]

limit = 240
solution(people,limit)

# 3명도 탈 수 있는 건 줄 알고 이렇게 짰다.
# 하지만 2명까지만 탈 수 있음. 그래서 2명 조건을 추가한다해도 시간초과뜸
