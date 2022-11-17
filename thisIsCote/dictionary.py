data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# in 으로 key가 있는지 따질 수 있다.
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

print(data.keys())
print(data.values())