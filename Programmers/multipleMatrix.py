# [프로그래머스] 행렬의 곱셈
def solution(arr1, arr2):
    answer = []
    # arr1 InnerArr Len = arr2 Len
    rLen1 = len(arr1[0])
    # arr2 InnerArr Len
    rLen2 = len(arr2[0])
    
    for row in arr1:
        # one row of arr1
        tempArr = []
        for j in range(rLen2):
            sum = 0
            for index in range(rLen1):
                sum+=row[index]*arr2[index][j]
            tempArr.append(sum)
        answer.append(tempArr)
    
    return answer