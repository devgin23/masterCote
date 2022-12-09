# [프로그래머스] 햄버거 만들기
def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        if stack[-4:] == [1,2,3,1]:
            for j in range(4):
                stack.pop()
            answer += 1
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            for j in range(4):
                stack.pop()
            answer += 1
    return answer