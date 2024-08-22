# 버스의 시간표를 작성하는 프로그램을 코딩하라
# 첫 운행 시간은 오전 9시, 마지막 운행시간은 오후 6시라고 한다.
# 9 ~ 18 (9시와 18시가 포함)
# 배차 간격을 분 단위로 입력하면, 하루의 버스 운행시간을 출력하라.
# 예) 25

# 프로그램은 반복되게 하며,
# '계속하시겠습니까?'라고 묻고, y면 계속 아니면 종료한다.
play_1 = True
while play_1 :
    hour = 9
    min = 0
    배차간격 = int(input('배차 간격을 입력하세요 : ')) 

    play = True
    while play:
        if hour == 18 and min > 0:
            play = False 
        else:
            print(f'{hour}시 {min}분')
            min = min + 배차간격
            if min >= 60:
             hour = hour + 1
             min = min - 60     

    user = input('계속하시겠습니까? : ')   
    if user != 'y':
        play_1 = False


