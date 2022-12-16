#[프로그래머스] 피보나치 수
def solution(n):
    answer = 0
    num = [0,1]
    for i in range(2,n+1):
        num.append((num[i-2]+num[i-1])%1234567)
    answer = num[-1]
    print(answer)
    return answer

solution(5)