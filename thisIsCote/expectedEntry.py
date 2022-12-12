# [프로그래머스] 예상 대진표
from math import ceil
def nextNum(num):
    num = ceil(num/2)
    return num
def solution(n,a,b):
    answer = 1
    # 2,3일 때 1차이가 난다고 바로 만나는 것은 아니다.
    while abs(a-b) != 1 or nextNum(a) != nextNum(b):
        a = nextNum(a)
        b = nextNum(b)
        answer += 1
    
    return answer