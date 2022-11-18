# 파이썬에서는 코드의 Block을 들여쓰기(Indent)로 지정합니다.
x = 15

if x >= 10:
    print("x>=10")
if x>=0:
    print("x>=0")
if x>= 30:
    print("x>=30")

# 파이썬에서는 if ~ elif ~ else 이다.

a = -7
if a>=0:
    print("a>=0")
elif a>=-10:
    print("-10<a<0")
else:
    print("-10>a")