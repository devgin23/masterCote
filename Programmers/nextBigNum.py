# [프로그래머스]다음 큰 숫자

from collections import deque

def solution(n):
    answer = 0
    b = bin(n)[2:]
    que = deque(b)
    length = len(que)
    n1 = que.count('1')
    n0 = que.count('0')
    check1 = False
    if length == n1 :
        que.appendleft('1')
    elif n1 == 1 :
        que.append('0')
    else :
        pass
        




    print(que)
    print(answer)
    return answer

solution(17)