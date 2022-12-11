# [프로그래머스] 숫자의 표현
def solution(n):
    answer = 1
    # n이 들어오는 수
    for i in range(2,n):
        # 2부터 하나씩 본다.
        if i%2 == 0:
            # i가 짝수일 때[2,4,6]
            # k는 나누는 값에서 2를 제거했을 때
            k = i//2
            # 마지막에 홀수여야한다.
            if n%k == 0:
                if n//k < i:
                # 나눈 몫이 i보다 작다면 break
                    continue
                if (n//k)%2 == 1:
                    answer += 1
        else:
            # 나누는 수 i가 홀 수 일 때[3,5,7]
            # 나눠져야하고 그 몫이 
            k = i//2
            if n%i == 0:
                if n//i <= k:
                # 나눈 몫이 i보다 작다면 break
                    continue
                answer += 1
            



    return answer

