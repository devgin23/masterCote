# 3003

listA = list(map(int,input().split()))
listB = [1,1,2,2,2,8]

result = list(map(lambda b, a : b-a, listB, listA))
for i in result:
    print(i, end=" ")