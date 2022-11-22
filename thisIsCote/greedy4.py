# 모험가 길드 : 문제 조건

N = int(input())
fear = list(map(int,input().split()))
fear.sort()
answer = 0
nowPartyNum = 0
for i in range(0,N):
    needsNum = fear[i]
    nowPartyNum += 1
    if needsNum <= nowPartyNum:
        nowPartyNum = 0
        answer += 1
print(answer)