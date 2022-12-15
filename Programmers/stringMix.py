# [프로그래머스] 문자열 내 마음대로 정렬하기
from collections import defaultdict
def solution(strings,n):
    answer = []
    dic = defaultdict(list)
    strings.sort()
    for i in strings:
        dic[i[n]].append(i)
    
    sortedDic = sorted(dic)

    for i in sortedDic:
        for j in dic[i]:
            answer.append(j)
    return answer

strings = ["sun","bed","car","caar"]
n = 1
solution(strings, n)