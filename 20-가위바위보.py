# 컴퓨터와 사용자가 가위, 바위, 보 게임을 합니다.
# 컴퓨터는 random으로 가위, 바위, 보를 선택학,
# 사용자는 가위 바위 보 중 하나를 입력한다.

# 예) : 0: 가위 1:바위, 2: 보 라고 정의할 수 있다.

# 매 가위, 바위, 보 마다 컴퓨터는 무엇, 사용자는 무엇, 승자를 판정하고,
# 게임을 계속하시겠습니까? 라고 묻고. y이면 계속하고, 아니면 종류한다.
# 최종 결과는 컴퓨터 : 몇승 , 사용자 : 몇승을 출력해준다.
    
import random

RCP = """
--- 가위 바위 보 게임하기 ---
가위 : 0
바위 : 1
보  : 2
"""

num_list = ['가위', '바위', '보']
com_score = 0
user_score = 0
draw_score = 0

play = True
while play :
    print(RCP)
    computer = random.randint(0,2)

    user = int(input('\n무엇을 내시겠습니까? : '))

    print(f'컴퓨터는 {num_list[computer]}를 냈고, 당신은 {num_list[user]}를 냈습니다.')
    if user == computer :
        print('\n무승부입니다.')
        draw_score = draw_score + 1
       
    elif (computer == 0 and user == 2) or (computer == 1 and user == 0) or (computer == 2 and user == 1) :
        print('\n컴퓨터가 이겼습니다.')
        com_score = com_score + 1
    else:
        print('\n당신이 이겼습니다')
        user_score = user_score + 1
    user1 = input('\n게임을 계속하시겠습니까? : ')
    if user1 == 'y':
        play = True
    else:
        play = False
print(f"""
      ---게임의 최종 결과는---

        컴퓨터: {com_score}승 
        사용자 : {user_score}승 
        무승부 : {draw_score}번
       """)
    
        