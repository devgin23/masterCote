# [프로그래머스] 올바른 괄호
from collections import deque
def solution(s):
    answer = False
    s = deque(s)
    pringle = []
    length = len(s)
    for i in range(length):
        pop = s.popleft()
        pringle.append(pop)
        if pringle[-2:] == ['(',')']:
            pringle.pop()
            pringle.pop()
    if pringle == []:
        answer = True
    
    return answer

# 다른 사람 풀이
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0