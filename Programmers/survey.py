# [프로그래머스] 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    score = dict()
    for i in ['R','T','C','F','J','M','A','N']:
        score[i]=0
    
    for i in range(len(survey)):
        # survey
        # choices
        if choices[i] in [1,2,3]:
            score[survey[i][0]] += 4-choices[i]
        elif choices[i] in [5,6,7]:
            score[survey[i][1]] += choices[i]-4
    
    if score['R'] >= score['T']:
        answer+='R'
    else:
        answer+='T'
    if score['C'] >= score['F']:
        answer+='C'
    else:
        answer+='F'
    if score['J'] >= score['M']:
        answer+='J'
    else:
        answer+='M'
    if score['A'] >= score['N']:
        answer+='A'
    else:
        answer+='N'
    return answer