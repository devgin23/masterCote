# [이코테] 선택 정렬
# 선택 정렬 : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다.

array = [3,0,8,7,4,9,1,6,2,5]
leng = len(array)

for i in range(leng):
    min_index = i
    for j in range(i+1, leng):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)