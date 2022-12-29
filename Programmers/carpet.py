# [프로그래머스] 카펫
def solution(brown, yellow):
    answer = []
    totalSqrNum = brown+yellow
    divNum = []
    maxNum = (brown-2)//2
    minNum = (brown-4)//4+2
    rangeNum = list(range(minNum,maxNum+1))
    for i in range(1,totalSqrNum+1):
        if totalSqrNum%i == 0:
            if i in rangeNum :
                divNum.append([i,totalSqrNum//i])
    # 나온 가로 세로 길이 쌍을 각각 -2하고 서로 곱했을 때 노란사각형의 갯수가 나와야한다.
    for i in divNum:
        if (i[0]-2) * (i[1]-2) == yellow:
            answer = i
    return answer
solution(10,2)