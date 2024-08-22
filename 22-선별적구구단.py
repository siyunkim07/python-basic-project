#  사용자로 부터 입력을 받은 구구단의 '단'을 출력하되,
# 곱셈의 결과 홀수 혹은 짝수 혹은 전체를 선택하서 출력하도록 코딩하라.

# 힌트 : 두개의 input을 받는다.



play = True
while play :
    user = int(input('숫자를 입력하세요. : '))
    user_1 = input('범위(홀수, 짝수, 전체 중 택1)를 고르세요 : ')
    for i in range(1,10):
        result = user * i
        if user_1 == '전체':
            print(f'{user} x {i} = {result}')
        elif user_1 == '홀수':
            if result % 2 == 1:
             print(f'{user} x {i} = {result}')
        elif user_1 == '짝수':
            if result % 2 == 0:
             print(f'{user} x {i} = {result}')
    user_2 = input('종료하시겠습니까? : ')
    if user_2 == '네':
       play = False
    