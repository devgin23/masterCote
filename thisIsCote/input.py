# n = int(input())
# # input받은 값을 공백을 기준으로 나눠 리스트를 만들고, 리스트 항목 모두에 int형으로 바꿔준다 그걸 리스트로 만든다.
# data = list(map(int,input().split()))

# print(n)
# print(data)

# 빠르게 입력받기

import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)