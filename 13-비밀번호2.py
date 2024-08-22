import random

password = 'A!1234'

seed = str(random.randint(1,5))

password = password + seed

print(password)



play = True
while play:
     pw = input('비밀번호를 입력하세요 : ')

     if pw == password:
      print('비밀번호가 맞습니다.')
      play = False

     else:
        print('비밀번호가 틀립니다.')