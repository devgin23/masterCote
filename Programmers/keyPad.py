# [프로그래머스] 키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    ld = 0
    rd = 0
    
    for i in numbers:
        if i == 0 : i = 11
        for j in keypad:
            for k in j:
                if i == k:
                    rowC = i



    return answer