# [프로그래머스]다음 큰 숫자

from collections import deque

def solution(n):
    answer = 0
    # n을 2진수 str으로 변환
    b = bin(n)[2:]
    print(b)
    # que에 2진수str으로 변환해서 풀이
    que = deque(b)
    tempList = list()
    length = len(que)
    # 1의 개수를 세어 이에 따라 분기
    n1 = que.count('1')    
    if length == n1 :
        # 1111 -> 10111
        que.popleft()
        que.appendleft('0')
        que.appendleft('1')
    elif n1 == 1 :
        # 1000 -> 10000
        que.append('0')
    else :
        # 1100110 -> 1101001
        cnt1 = 0
        flag = True
        while que:
            pop = que.pop()
            if pop == '1':
                cnt1 += 1
            tempList.append(pop)

            if pop == '0' and cnt1 > 0:
                flag = False
                break
        tempList.sort(reverse=True)
        tempQ = deque(tempList)       
        que.append(tempQ.popleft())
        # 110 -> 1001
        if flag: que.append('0')
        while tempQ:
            que.append(tempQ.pop())
        




    print(que)
    binStr = ('').join(que)
    answer = int(binStr,2)

    print(answer)
    return answer

solution(6)