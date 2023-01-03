# [프로그래머스] 최소 공배수
def solution(arr):
    answer = 0
    arr.sort(reverse = True)
    print(arr)
    stop = False
    maxNum = 0
    multi = 1
    while not stop :
        maxNum = arr[0]*multi
        for i in arr:
            if maxNum % i != 0 :
                stop = False
                break
            stop = True
        multi += 1
    answer = maxNum
    print(answer)
    return answer

arr = [2,6,8,14]

solution(arr)


### 위에가 지수씨 아이디어로 짠 코드
### 아래가 프로그래머스의 다른 사람의 풀이

from fractions import gcd


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer