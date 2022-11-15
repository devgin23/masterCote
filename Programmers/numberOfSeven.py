# 프로그래머스 7의 개수
# array 에 담긴 정수들 중 7의 개수를 리턴하는 함수 만들기.

def solution(array):
    answer = 0
    for a in array:
        # array의 하나하나를 봄.
        c = 10
        if a%c == 7:answer+=1 # 1의 자리가 7이면 answer++
        while a//c!=0: # 다음 위의 자리수가 존재한다면
            if ((a//c)%10)==7:answer+=1 # 다음 위의 자리수가 7이라면 answer++ 
            c *= 10 # 다음 while 비교에서는 100, 1000, 10000의 자리 비교하도록
    return answer

print(solution({7,77,17}))