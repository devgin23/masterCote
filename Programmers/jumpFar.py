# [프로그래머스] 멀리 뛰기
# 2의 위치를 정해주는 것과 같다. (2가 여러개일 때의 조합)
from math import factorial
def solution(n):
    #2의 개수가 0일 때는 세지않고 answer = 1부터 시작.
    answer = 1
    limit = n//2
    if n == 1:
        return answer %1234567
    elif n == 2:
        return 2 % 1234567
    #2의 개수를 1부터 증가시키며 for문을 돌린다.(i=2의 개수)
    for i in range(1,n):
        # n=5일때 짝이 3명부터는 안이루어지니까 반복문 종료.
        if i>limit: break
        # 짝의 개수에 따른 자리 수
        space = n-i
        a = factorial(space)%1234567
        b = factorial(space-i)%1234567
        c = factorial(i)%1234567
        case = int(a/b/c)
        answer += case
    print(answer)
    return answer
# 피보나치 수열로 푼 풀이.
def solution02(n):
    answer = 0
    num = [0]*2000
    num[0] = 1
    num[1] = 1
    for i in range(2,n+1):
        num[i] = (num[i-2]+num[i-1])%1234567
    answer = num[n]
    return answer
# [프로그래머스] 피보나치 수열 풀이 가져옴.
def solution(n):
    answer = 0
    num = [1,1]
    for i in range(2,n+1):
        num.append((num[i-2]+num[i-1])%1234567)
    answer = num[-1]
    print(answer)
    return answer


solution(6)