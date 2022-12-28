# [프로그래머스] 디펜스 게임
def solution01(n, k, enemy):
    answer = 0

    for i in range(1,len(enemy)+1):
        flagBreak = False
        limitEnemy = enemy[0:i]
        limitEnemy.sort()
        if len(limitEnemy)<k:
            answer += 1
            continue
        for j in range(k):
            limitEnemy.pop()
        sumA = sum(limitEnemy)
        if sumA > n:
            flagBreak = True
        if flagBreak : break
        answer += 1
    print(answer)
    return answer
n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
#solution01(n, k, enemy)

############ 위의 것은 답은 맞지만 속도가 느려 실패뜸.테스트케이스3,4,6,7,8,9,10(초기단계) ###############
############ 아래 것은 조금 개선해서 3,6,7,8,9,10 실패 ###############
def solution(n, k, enemy):
    answer = k-1
    length = len(enemy)
    if k >= length: return length
    for i in range(k,length+1):
        flagBreak = False
        limitEnemy = enemy[0:i]
        limitEnemy.sort()
        for j in range(k):
            limitEnemy.pop()
        sumA = sum(limitEnemy)
        if sumA > n:
            flagBreak = True
        if flagBreak : break
        answer += 1
    
    return answer

######################## heap을 쓴다고해도 로직이 시간복잡도가 높아 시간초과가 뜬다.####################
import heapq
def solution03(n, k, enemy):
    answer = k-1
    length = len(enemy)
    if k >= length: return length
    for i in range(k,length+1):
        flagBreak = False
        tempN = n
        limitEnemy = [-j for j in enemy[0:i]]
        sumA = -sum(limitEnemy)
        heapq.heapify(limitEnemy)
        for j in range(k):
            sumA = sumA + heapq.heappop(limitEnemy)
        
        if sumA > n:
            flagBreak = True
        if flagBreak : break
        answer += 1
    print(answer)
    return answer
n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]


##################### 아래 것이 성공한 것. ########################
# 하나씩 넣어가며 작을 때 가장 큰 값을 무적권 쓴걸로 함.
def solution00(n, k, enemy):
    answer = 0
    length = len(enemy)
    if k >= length: return length
    max_e = []
    sumA = 0
    for e in enemy:
        heapq.heappush(max_e, (-e, e))
        n -= e
        if n<0 and k > 0:
            n+=heapq.heappop(max_e)[1]
            k -= 1
            if n < 0 :
                print(answer)
                return answer
        if n<0 and k == 0 :
            print(answer)
            return answer
        answer += 1
        

    print(answer)
    return answer
n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
solution00(n, k, enemy)