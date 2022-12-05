# [프로그래머스] 키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    # 왼손,오른손으로부터 눌러야하는 번호까지의 거리
    ld = 0
    rd = 0
    # 왼손의 마지막 위치 index로 기억
    rowBL = 3
    colBL = 0
    # 오른손의 마지막 위치 index로 기억
    rowBR = 3
    colBR = 2
    # 눌러야 하는 번호의 위치 index
    rowC = 0
    colC = 0
    for i in numbers:
        if i == 0 : i = 11
        for j in range(len(keypad)):
            for k in range(len(keypad[j])):
                # 키패드 하나씩 비교하는거야.
                # i 는 numbers 에서 온 번호 1개
                # k 는 각 키패드 번호 1개
                if i == keypad[j][k]:
                    rowC = j
                    colC = k
        
        if i in [1,4,7]:
            answer += 'L'
            rowBL = rowC
            colBL = colC
        elif i in [3,6,9]:
            answer += 'R'
            rowBR = rowC
            colBR = colC
        else :
            ld = abs(rowBL-rowC)+ abs(colBL-colC)
            rd = abs(rowBR-rowC)+ abs(colBR-colC)
            if ld>rd:
                answer+= 'R'
                rowBR = rowC
                colBR = colC
            elif ld<rd:
                answer+= 'L'
                rowBL = rowC
                colBL = colC
            elif ld == rd:
                if hand == 'left':
                    answer+= 'L'
                    rowBL = rowC
                    colBL = colC
                else :
                    answer+= 'R'
                    rowBR = rowC
                    colBR = colC

        



    return answer

solution([1,2,3,4,5,0,9,8,6], 'left')