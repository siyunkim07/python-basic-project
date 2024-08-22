# 1. 반지름을 입력 받아서, 원의 넓이와 원의 둘레를 구하라



result = float(input('반지름을 입력하세요. : '))
wide = (result ** 2) * 3.14
round = (result * 2) * 3.14
print(f'원의 넓이는 {wide:.2f}이고, 원의 둘레는 {round:.2f}입니다.')