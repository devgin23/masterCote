# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다.
N = int(input())
navi = list(input().split())

x, y = 1, 1
for i in navi:
    if i == 'R':
        x += 1
        if x > N or x < 1:
            x -= 1
    elif i == 'U':
        y -= 1
        if y > N or y < 1:
            y += 1
    elif i == 'D':
        y += 1
        if y > N or y < 1:
            y -= 1
    elif i == 'L':
        x -= 1
        if x > N or x < 1:
            x += 1
print(x,y)