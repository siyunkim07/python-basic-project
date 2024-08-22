# split()을 이용해서 입력값을 list로 만들고, 언팩킹해서 변수에 할당

result = input('곱셈할 두 수를 입력하세요 : ').split(" ")
a, b = result  # 문자열

print(f'{a} x {b} = {int(a) * int(b)}')

