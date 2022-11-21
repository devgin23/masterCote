# [LJ003] 2022.11.21 : [이코테] 그리디 유형 문제 풀이
# 곱하기 혹은 더하기: 문제 해결 아이디어

st = input()
result = int(st[0])
for i in range(0,len(st)-1):
    if int(result ==0 or result == 1 or int(st[i+1]) == 0 or int(st[i+1]) == 1):
        result += int(st[i+1])
    else:
        result *= int(st[i+1])
print(result)