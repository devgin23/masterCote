# sum()
result = sum([1,2,3,4,5])
print(result)

# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

# eval()
# 사람의 입장에서 표현된 수식을 계산해준다? 잘 모르겠다.
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 50), ('이순신',32),('아무개',74)]
result = sorted(array, key=lambda x:x[1], reverse=True)
print(result)


# 순열과 조합. (itertools)
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것

from itertools import permutations
from itertools import combinations

data = ['A','B','C']

result = list(permutations(data,2))
print(result)
result = list(combinations(data,2))
print(result)

# 중복 순열(product), 중복 조합(combinations_with_replacement)

# 최대 공약수, 최소 공배수
import math

# 최소 공배수(LCM)을 구하는 ㅎㅁ수
def lcm(a,b):
    return a*b//math.gcd(a,b)

a = 21
b = 14
print(math.gcd(a,b)) # 최대 공약수 (GCD) 계산
print(lcm(a,b)) # 최소 공배수 (LCM) 계산

