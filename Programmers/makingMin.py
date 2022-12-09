# [프로그래머스] 최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        
        answer += A.pop()*B.pop()
        

    return answer