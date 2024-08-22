# 카페의 메뉴를 관리하는 프로그램이다. 
# 메뉴관리 기능은, 

# 1. 메뉴 출력
# 2. 메뉴 추가
# 3. 메뉴 삭제
# 4. 메뉴 이름 변경
# 5. 종료

# 카페의 초기 메뉴는,
# 리스트로, ['사과', '당근', '망고']이다.

# 메뉴관리 기능을 선택한 다음, 각 기능을 구현하라.

flavor = []
def read_menu():
    f = open("카페메뉴.txt", 'r', encoding='utf8')
    lines = f.readlines()
    idx = 0
    for line in lines:
        flavor = line.strip()
        flavor[idx] = menu
        idx = idx + 1
    f.close()

def write_menu():
    f = open("카페메뉴.txt", 'w', encoding='utf8')
    for  i in flavor:
        data = f'{i}\n'
        f.write(data)
    f.close()

def display_menu():
    for i in flavor:
         print(f'{i}주스')

play = True
while play:
    menu = """
    1. 메뉴 출력
    2. 메뉴 추가
    3. 메뉴 삭제
    4. 메뉴 이름 변경
    5. 종료
    """
    print(menu)

    user = input('\n메뉴를 보고 선택하세요 : ')
    if user == '1':
        write_menu()
        display_menu()
    elif user == '2':
        add = input('추가하고 싶은 맛을 입력하세요 : ')
        if add in flavor:
            print('이미 있는 맛입니다.')
        else:
            flavor.append(add)
            write_menu()
            display_menu()
    elif user == '3':
        delete = input('삭제하고 싶은 맛을 입력하세요 : ')
        if delete in flavor:
            flavor.remove(delete)
            write_menu()
            display_menu()
        else:
            print('메뉴에 없는 맛입니다.')
    elif user == '4':
        old,new = input('어떤 맛을 어떤 맛으로 바꾸시겠습니까?').split(' ')
        for i,j in enumerate(flavor):
            if j == old:
                flavor[i] = new 
                break
        write_menu()
        display_menu()
    elif user == '5':
        print('프로그램을 종료합니다.')
        play = False

    
