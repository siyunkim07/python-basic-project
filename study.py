# 딕셔너리

dic = { 
    '사과' : 5,
    '귤' : 3,
    '감' : 4
}

# 딕셔너리 값을 참조

print(dic['사과'])
print(dic['귤'])
print(dic['감'])

# 딕셔너리 값을 변경

dic['사과'] = 10
print(dic['사과'])

# 딕셔너리 for문

for i in dic:
    print(i)

for i in dic.values():
    print(i)

for i,j in dic.items():
    print(i,j)



# 딕셔너리에 새로운 속성을 추가하는 방법

dic['고구마'] = 4 # 딕셔너리에 해당 키가 없으면 새로운 속성이 추가된다..

for i, j in dic.items():
    print(i, j)


# 딕셔너리의 속성을 제거하는 방법

del dic['고구마']

# 딕셔너리에 특정 키가 있는지 검사

print('고구마' in dic)