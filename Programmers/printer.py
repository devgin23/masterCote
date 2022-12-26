# [프로그래머스] 프린터

from collections import deque
from collections import defaultdict
def solution(priorities, location):
    
    answer = 0
    # make number of priority dict
    dictPrio = defaultdict(int)
    for i in priorities:
        dictPrio[i] += 1
    # make priority que
    que = deque(priorities)
    # make index que
    index = deque(range(len(que)))
    while que :
        flagPass = False
        nowPrint = que[0]
        index0 = -1
        for i in range(nowPrint+1,10):
            if dictPrio[i]>0:
                flagPass = True
        if flagPass :
            que.rotate(-1)
            index.rotate(-1)
        else :
            dictPrio[que.popleft()] += -1
            answer += 1
            index0 = index.popleft()
        
        if index0 == location and flagPass == False:
            break
    return answer