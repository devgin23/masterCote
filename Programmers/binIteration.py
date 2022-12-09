# [프로그래머스] 이진 변환 반복하기
def solution(s):
    answer = []
    cnt1st = 0
    cnt = 0
    while s != '1':
        lenA = len(s)
        s = s.replace('0','')
        lenB = len(s)
        cnt += lenA-lenB
        s = str(format(lenB,'b'))
        cnt1st += 1
    answer.append(cnt1st)
    answer.append(cnt)
    return answer

# 처음 풀었을 때
# 시간 초과가 떴음.
def solution(s):
    answer = []
    sList = list(s)
    cnt = 0
    cnt1st = 0
    prt = ''
    while prt != '1':
        for i in range(len(sList)):
            if '0' in sList:
                sList.remove('0')
                cnt += 1
        prt = str(format(len(sList), 'b'))
        sList = list(prt)
        cnt1st += 1
    answer.append(cnt1st)
    answer.append(cnt)
    return answer