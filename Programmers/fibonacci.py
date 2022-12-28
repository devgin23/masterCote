#[프로그래머스] 피보나치 수
import time
def solution(n):
    start = time.time()
    answer = 0
    num = [0,1]
    for i in range(2,n+1):
        num.append((num[i-2]+num[i-1])%1234567)
    answer = num[-1]
    print(answer)
    end = time.time()
    print(str((end-start)*1000) + ' ms')
    return answer

# solution02가 더 빠르다. append를 쓰기보다는 배열을 크게 만들어놓고 인덱스로 넣는 것이 더 빠름.
def solution02(n):
    start = time.time()
    answer = 0
    num = [0]*(n+2)
    num[0]=0
    num[1]=1
    for i in range(2,n+1):
        num[i] = ((num[i-2]+num[i-1])%1234567)
    answer = num[n]
    print(answer)
    end = time.time()
    print(str((end-start)*1000) + ' ms')
    return answer
solution(1000000)