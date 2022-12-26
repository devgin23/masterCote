import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
# scoville이 heap 자료구조로 변경 되었어도 min함수로 최솟값을 찾는 것은 시간복잡도 O(N) 이다.
# heap 자료구조로 최소값을 찾는 시간 복잡도는 O(logN)이다.
#     while min(scoville) < K: 
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer
