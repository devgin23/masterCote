# [프로그래머스] 영어 끝말 잇기
# 몇번째 사람이 몇번째 바퀴에 걸리는지 return
# 안걸리면 [0,0] return
def solution(n, words):
    answer = [0,0]
    wordsSet = set()
    index = 0
    turn = 1
    prevEnd = ''
    for i in words:
        if index >= n:
            index -= n
            turn += 1
        index += 1
        length = len(wordsSet)
        wordsSet.add(i)
        if index == 1 and turn == 1:
            prevEnd = i[-1]
            continue
        if length == len(wordsSet) or prevEnd != i[0]:
            return [index,turn]
        prevEnd = i[-1]

    print(answer)
    return answer
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
solution(n,words)


### 위에는 len(set자료형) 비교해서 푼 내 풀이
## 아래는 깔꼼쓰한 다름 사람 풀이

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]