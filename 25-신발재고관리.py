# 23, 24번을 이용해서,
# 신발의 재고관리 프로그램을 작성하라. 

# 1. 입고 : 기존 재고에 새로운 수량을 추가
# 2. 출고 : 기존 재고에 수량을 빼는 것.

# 메뉴(기능)를 선택해서 - 입고 or 출고
# 수량을 입력 

# 프로그램을 종료할 때까지 계속 반복되도록.

stock ={ 
 '240' : 14,
 '245' : 20,
 '250': 11,
 '255': 14,
 '260' : 28,
 '265' : 32,
 '270' : 17,
 '275' : 9
}

play = True
while play:
    입고_출고 = input('입고와 출고중 하나를 선택하세요 : ') 

    if 입고_출고 == '출고':
        size,num = input('사이즈와 숫자를 입력해주세요(숫자만 입력) : ').split(" ")
        num = int(num)

        if size in stock:
            if stock[size] >= num:
                stock[size] = stock[size] - num
                for i in stock:
                    print(f'{i}mm : {stock[i]}개')
            else:
                print(f'제고가 없습니다. 현 재고는 {stock[size]}개 입니다.')
        else:
            print('입력한 사이즈가 없습니다.')

    elif 입고_출고 == '입고' :
        size,num = input('사이즈와 숫자를 입력해주세요(숫자만 입력) : ').split(" ")
        num = int(num)

        if size in stock:
            print('입력한 사이즈의 수량을 추가합니다.')
            if stock[size] + num <= 30:
                stock[size] = stock[size] + num
                for i in stock:
                    print(f'{i}mm : {stock[i]}개')
            else:
                print(f'현재 재고는 {stock[size]}개 + 수량{num}개로 30개를 초과하였습니다.')

        else:
            print('입력한 사이즈의 신발을 추가합니다.')
            if num <= 30 :
                stock[size] = num
                for i in stock:
                    print(f'{i}mm : {stock[i]}개')
            else:
                print(f'수량{num}개가 30개를 초과합니다.')      
                         
    user = input('계속 하시겠습니까(예 or 아니요) : ')
    if user != '예':
        play = False