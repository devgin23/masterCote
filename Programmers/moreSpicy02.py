import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while min(scoville) < K:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer
