#[LJ006] 2022.11.28 : [이코테] DFS&BPS / Stack, Que 학습
# 재귀 함수 (Recursive Function) 란 자기 자신을 다시 호출 하는 함수를 의미합니다.
# 단순한 형태의 재귀 함수 예제

def recursive_function(i):
    if i  == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 함수를 종료합니다.')

recursive_function(1)