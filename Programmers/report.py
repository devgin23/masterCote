# [프로그래머스]신고 결과 받기

def solution(id_list,report,k):
    answer = []

    # report 중복 없애기   
    set_report = set(report)
    # 신고 당한 갯수 dict 만들기
    numDic = dict()
    # 신고 한 애들의 배열 dict 만들기
    listDic = dict()
    # answer로 낼 메일 받은 dict 만들기
    answerDic = dict()
    for i in id_list:
        numDic[i] = 0
        listDic[i] = []
        answerDic[i] = 0
    for i in set_report:
        reporter, reported = i.split()
        numDic[reported] += 1
        # b를 신고한 애가 a, c 가 있다. 신고당한애가 Key, 신고한 애들이 Value
        listDic[reported].append(reporter)
    list = []
    for i in numDic.keys():
        if numDic[i]>=k:
            list.append(i)
    # 정지 당한 애 한명
    for i in list:
        # 걔를 신고한 애들의 리스트
        for j in listDic[i]:
            answerDic[j] += 1
    for i in answerDic:
        answer.append(answerDic[i])
    return answer

solution(['a','b','c'], ['a b','b c','c a','c b','a b'], 2)