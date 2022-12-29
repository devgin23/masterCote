# [프로그래머스] 점프와 순간이동
def solution(n):
    jump = 0
    while n != 0:
        if n%2 == 1:
            n -= 1
            jump+=1
        else:
            n = n//2
            
    print(jump)
    return jump
solution(5000)