# 함수

# 함수를 사용하면 소스코드의 길이를 줄일 수 있다.
    # 매개변수 : 함수 내부에서 사용할 변수
    # 반환 값 : 함수에서 처리 된 결과를 반환 (return)

def add(a,b):
    return a+b
print(add(3,7))
# 람다 표현식
# 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.

print((lambda a, b : a + b)(3,7))

# 람다 표현식 예시 : 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신',32),('아무개',74)]
def my_key(x):
    return x[1]
print(sorted(array, key = my_key))
print(sorted(array, key = lambda x: x[1]))

# 람다 표현식 예시 : 여러 개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b : a+b, list1, list2)
print(list(result))
# map은 각각의 원소에 함수를 적용시킬 때 사용

# global 키워드
# 함수 바깥 변수를 쓰려면 global 키워드를 무조건 써줘야한다.
# 전역변수를 참조만 하는 것은 오류가 나지 않지만
# 전역변수를 변경하려하면 global 키워드가 필수이다.
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()
print(a)


######################################
# 동일명의 경우 바깥에서는 전역변수를 우선 안에서는 지역변수를 우선한다.
array = [1,2,3,4,5]

def func():
    array = [3,4,5]
    array.append(6)
    print(array)

func()
print(array)

