# 왕실의 나이트 : 문제 설명
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력.

# ex) c2에 있을 때 이동할 수 있는 경우의 수는 6가지 입니다.

# 8x8이다.
def check(x, y):
    rtn = False
    if x in range(8):
        if y in range(8):
            rtn = True 
    return rtn

position = input()
col = position[0]
if col == 'a': col = 0
elif col == 'b': col = 1
elif col == 'c': col = 2
elif col == 'd': col = 3
elif col == 'e': col = 4
elif col == 'f': col = 5
elif col == 'g': col = 6
elif col == 'h': col = 7
# 위 코드를 아스키코드로 하는 법.
# col = int(ord(position[0])-int(ord('a')) + 1
row = int(position[1])
row -= 1

move = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count = 0
for i in move:
    tempR = row + i[0]
    tempC = col + i[1]
    if check(tempR, tempC): count+=1
print(count)