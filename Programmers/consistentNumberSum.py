# [LJ002] 2022.11.18 : 프로그래머스 연속된 수의 합

def solution(num, total):
    answer = []
    centerNum =0
    if num % 2 ==0:
        centerNum = (total//(num//2))//2
        answer = list(range(centerNum-(num//2-1),centerNum+(num//2+1)))
    else :
        centerNum = total//num
        answer = list(range(centerNum-((num-1)//2),centerNum+1+((num-1)//2)))

    print(answer)
    return answer

solution(4, 14)