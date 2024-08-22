stock ={}
def read_size():
    f = open("신발재고.txt", 'r', encoding='utf8')
    lines = f.readlines()
    for line in lines:
        size,num = line.strip().split(':')
        stock[size] = int(num)
    f.close()

def write_size():
    f = open("신발재고.txt", 'w', encoding='utf8')
    for  i,j in stock.items():
        data = f'{i}:{j}\n'
        f.write(data)
    f.close()

def displayShoes():
    for i in stock:
        print(f'{i}mm : {stock[i]}개')

read_size()

play = True
while play:
    menu = """
    1. 상품등록
    2. 입고(+)
    3. 출고(-)
    4. 상품삭제 
    5. 상품보기
    6. 종료
    """
    print(menu)
    user = int(input('메뉴를 보고 선택을 하세요 : '))

    if user == 1:
        size = input('새로운 사이즈를 등록해주세요(숫자만 입력) : ')
        if size in stock:
            print('이미 있는 사이즈입니다.')
        else:
            stock[size] = 0
            write_size()
            displayShoes()

    elif user == 2:
        size,num = input('사이즈와 숫자를 입력해주세요(숫자만 입력) : ').split(" ")
        num = int(num)
        if size in stock:
            print('입력한 사이즈의 수량을 추가합니다.')
            if stock[size] + num <= 30:
                stock[size] = stock[size] + num
                write_size()
                displayShoes()
            else:
                print(f'현재 재고는 {stock[size]}개 + 수량{num}개로 30개를 초과하였습니다.')
        else:
            print('입력한 사이즈가 있지 않습니다.')

    elif user == 3:
        size,num = input('사이즈와 숫자를 입력해주세요(숫자만 입력) : ').split(" ")
        num = int(num)
        if size in stock:
            if stock[size] >= num:
                stock[size] = stock[size] - num
                write_size()
                displayShoes()
            else:
                print(f'제고가 없습니다. 현 재고는 {stock[size]}개 입니다.')
        else:
            print('입력한 사이즈가 없습니다.')
    elif user == 4:
        size = input('사이즈를 입력해주세요(숫자만 입력) : ')
        if size in stock:
            del stock[size]
            write_size()
            displayShoes()
        else:
            print('입력하신 사이즈가 존재하지 않습니다.')
    elif user == 5:
        f = open("신발재고.txt", 'r', encoding='utf8')
        lines = f.readlines()
        for line in lines:
            print(line,end = '')
        f.close()

    elif user == 6:
        print('종료합니다.')
        play = False
