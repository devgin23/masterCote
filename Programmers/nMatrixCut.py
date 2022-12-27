# [프로그래머스] n^2 배열 자르기

def solution(n,left,right):
    answer = []
    # 행렬 만들기
    arr = [[0]*n for i in range(n)]
    index = [[0]*n for i in range(n)]

    # 같은 크기의 index 행렬 만들기
    for i in range(n):
        for j in range(n):
            arr[i][j] = max(i,j)+1
            index[i][j] = i*n + j

            if left <= index[i][j] <= right:
                answer.append(arr[i][j])
    # 2중 for문 돌며 left,right 범위에 따른 애들 뽑아 answer 만들기.


    print(arr)
    print(index)
    print(answer)
    return answer

solution(5,1,5)
#################### 위 solution 시간초과. ###################
#################### 아래 solution 시간초과 통과. ###################
# answer 에 쓸 것들만 만들어서. 극한의 효율 추구.
def solution(n,left,right):
    answer = []

    # 필요한 행만 구해서 만든다.
    aLeft = left//n
    aRight = right//n
    for i in range(aLeft,aRight+1):
        for j in range(n):
            if left <= i*n + j <= right :
                answer.append(max(i,j)+1)
            else: continue    

    return answer