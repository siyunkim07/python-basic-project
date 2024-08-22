# 주어진 범위 내에서 숫자 하나가 컴퓨터에 의해 정해집니다( random함수 사용)
# 사용자는 숫자를 맞출 때까지 게임을 계속해야 합니다.
# 만약에, 정답 숫자보다 사용자가 입력한 숫자가 클 경우에는 ' 더 작은 수 입니다.' 출력해주고,
# 만약에, 정답 숫자보다 사용자가 입력한 숫자가 작을 경우에는 '더 큰 수 입니다.' 출력해준다.
# 정답이면, '정답입니다'를 출력하고, 게임이 종료됩니다.
# 총 몇번 만에 정답을 맞추었는지 출력해 줍니다.

# 숫자의 범위는 1~20사이로 합니다.

import random

computer = random.randint(0,20)
play = True
score = 0
while play:
    score = score + 1
    user = int(input('숫자를 입력하세요. : '))
    if user > computer:
        print('더 작은 수 입니다.')
    elif user < computer:
        print('더 큰 수 입니다.')
    elif user == computer: 
        print('정답입니다!')
        play = False
        print(f'정답은 {computer}였습니다.')
        print(f'당신은 {score}번 만에 정답을 맞추었습니다.')