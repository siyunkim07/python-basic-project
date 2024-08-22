# 사용자로 부터 구구단 몇단을 출력할 것인지를 입력받는다.

# 결과는 다음과 같이 출력한다.

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8



play = True 
while play:
    user = int(input('구구단 몇단을 출력하시겠습니까? : '))
    for i in range(1,10):
        print(f'{user} x {i} = {user * i}')

    

   
  
   