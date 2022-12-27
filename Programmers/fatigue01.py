#[프로그래머스] 피로도
from itertools import permutations, combinations
# 이진희가 푼 것.
def solution01(k, dungeons):
    answer = -1
    perm = list(permutations(dungeons))
    for i in perm:
        # 던전 조합 하나 i
        curAns = 0
        tempK = k
        for j in i:
            # 던전 1개
            if j[0] <= tempK:
                curAns += 1
                tempK -= j[1]
            else:
                break
        if curAns > answer : answer = curAns
        
    return answer

dungeons = [[80,20],[50,40],[30,10]]
k = 80
# dfs 등으로 푼 다른 사람의 풀이가 많다. 다른 것도 알아보자.
# 최대 걸린 시간은 dfs가 더 크지만 대부분의 케이스에서 dfs가 월등히 더 빠르다.
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution02(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    # dfs 함수가 거의 전부이다.
    dfs(k, 0, dungeons)
    return answer
solution02(k, dungeons)