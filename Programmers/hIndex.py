# [프로그래머스] H-Index
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    hIndex = 0
    for i in citations :
        hIndex += 1
        if hIndex > i:
            answer = hIndex -1
            break
        if hIndex == i :
            answer = hIndex
            break
    print(answer)
    return answer

arr = [9,8,8,6,6,4,3,2,2,1,0]
solution(arr)