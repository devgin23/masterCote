# [프로그래머스] JadenCase 문자열 만들기
def solution(s):
    answer = ''
    s = s.lower()
    a = list(s)
    a[0] = a[0].upper()
    for i in range(len(a)):
        if a[i]==' ':
            if i+1 < len(a):
                a[i+1] = a[i+1].upper()
    answer = ('').join(a)
    return answer