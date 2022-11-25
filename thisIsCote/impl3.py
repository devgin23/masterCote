# 시각: 문제 조건
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 출력

# 3이 1개인 경우 : 
# 3이 2개인 경우 : 
# 3이 3개인 경우 : 
# 3이 4개인 경우 : 
# 시간이 3시인 경우 : 3600

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
print(count)