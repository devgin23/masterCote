# Python에서는 논리연산자를 || && ! 가 아닌 and or not 모두 문자로 이용한다.
# 기타 연산자가 있다.
# x in 리스트 : 리스트 안에 x가 들어가 있을 때 참(True)이다.
# x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 참(True)이다.

# 파이썬의 pass 키워드
# ex) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우
# 들여쓰기로 되어있는 블록을 기대하지만 없기때문에 코드가 없으면 오류가 난다.

a = 50

if a>= 30:
    pass
else :
    print("a<30")

# 조건부 표현식은 if ~ else문을 한 줄에 작성. (조건이 가운데 온다.)
score = 95
str = "Success" if score > 90 else "Fail"
print(str)