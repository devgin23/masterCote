def solution(scoville, K):
    answer = 0
    scoville.sort(reverse=True)
    que = scoville
    while True:
        if que[-1]>=K:
            break
        min1 = que.pop()
        min2 = que.pop()
        sum = min1 + min2*2
        que.append(sum)
        if len(que)==1 and que[-1]<K:
            answer = -1
            break
            
        que.sort(reverse=True)
        answer += 1
        
    return answer
