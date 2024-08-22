# 컴퓨터가 세개의 임의의 숫자를 선택합니다
# 사용자는 숫자 3개로 num1 * num2 - num3 식의 정답을 맞추면 됩니다.

# 예) 숫자가 3, 2, 1 일 경우, 화면에는 다음과 같이 출력하고, 사용자로 부터 정답을 입력 받습니다.
# 3 x 2 - 1 = 

# 각 숫자의 범위는 1, 9 까지 입니다.
# 정답을 맞힐때 마다 score는 1씩 증가합니다.
# 정답이 틀릴때까지 게임은 계속 됩니다.

import random

score = 0

play = True
while play:
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    num3 = random.randint(1,9)

    user = int(input(f'{num1} x {num2} - {num3} = '))
    sol = num1 * num2 - num3
    

    if sol == user:
        print('정답입니다. 점수 1점을 올립니다.')
        score = score + 1
        print(f'점수는 {score}점 입니다.')
    else:
        print('틀렸습니다. 게임을 종료합니다.')
        play = False    