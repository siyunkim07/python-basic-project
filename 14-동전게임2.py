# 동전게임은 컴퓨터가 동전을 던지고, 사용자는 컴퓨터가 던진 동전이 앞면인지 뒷면인지를 맞추는 게임이다.
# 컴퓨터는 random()함수를 이용해서 동전을 던지고, 사용자는 동정의 앞, 뒤를 입력한다.

# 앞, 뒤면의 구분은, 0 : 앞면, 1: 뒷면
# 컴퓨터가던진 동전의 면과 사용자가 입력한 동전의 면을 출력해주고, 
# 맞췄는지 틀렸는지를 결과를 출력하라.

# 참고) 사용자가 보고 선택할 수 있도록 menu를 출력해준다.

import random

play = True

print()
while play :

    menu = """
    0 : 앞
    1 : 뒤
    """
    print(menu)

    computer = random.randint(0,1)
    user = int(input('번호를 선택하세요 : '))

    if computer == 0:
        print('컴퓨터의 선택은 "앞"입니다 ')
    else : 
        print('컴퓨터의 선택은 "뒤"입니다')

    if user == 0:
        print('당신의 선택은 "앞"입니다')
    else:
        print('당신의 선택은 "뒤"입니다')

    print()
    if computer == user:
        print('축하합니다. 맞추었습니다')
        play = False
    else:
        print('애석합니다. 틀렸습니다.')


