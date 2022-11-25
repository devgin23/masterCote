ip = input()
num = 0
strNum = list(map(str,range(10)))
str1 = ''
for i in ip:
    if i in strNum:
        num += int(i)
    else: str1+=i
str1 = list(str1)
str1.sort()
str2 = ''
for i in str1:
    str2+=i
print(str2 + str(num))

# 위는 내가 푼 것.
#=========================================#
# 아래는 모범 답안

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data :
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else : 
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))