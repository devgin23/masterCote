# [LJ008] 2022.12.02 : [프로그래머스] 가운데 글자 가져오기
# 프로그래머스 : 가운데 글자 가져오기
def solution(s):
    answer = ''
    leng = len(s)
    if leng%2 ==0:
        center = leng//2
        answer = s[center-1:center+1]
    else:
        center = leng//2
        answer = s[center]
    return answer

print(solution(input()))