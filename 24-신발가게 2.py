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
size,num = input('사이즈와 숫자를 입력해주세요(숫자만 입력) : ').split(" ")
num = int(num)

if size in stock:
    print('입력한 사이즈를 추가합니다.')
    if stock[size] + num <= 30:
     stock[size] = stock[size] + num
     for i in stock:
        print(f'{i}mm : {stock[i]}개')
    else:
     print(f'현재 재고는 {stock[size]}개 + 수량{num}개로 30개를 초과하였습니다.')

else:
    if num <= 30 :
       stock[size] = num
       for i in stock:
          print(f'{i}mm : {stock[i]}개')
    else:
       print(f'수량{num}개가 30개를 초과합니다.')
    

     













    # if stock[size] + num <= 30:
    #  stock[size] = stock[size] + num
    #  for i in stock:
    #     print(f'{i}mm : {stock[size]}개')
    # else:
    #  print(f'현재 재고는 {stock[size]}개 + 수량{num}개로 30개를 초과하였습니다.')