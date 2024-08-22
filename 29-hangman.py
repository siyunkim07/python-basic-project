# 행맨은 영어 단어를 완성하는 게임
# 임의로 미리 등록된 단어를 대상으로 영어 단어를 완성하는 게임 
# 한번에 한 알파벳을 입력해서 몇번만에 단어를 완성하는가 하는 게임

import random 

eng_word = ['puppy', 'kitten', 'happy','illegal','universal','supenor','invention','female']
answer = random.choice(eng_word)

guess_letters = list("_" * len(answer))

life = 3
game_over = False

while not game_over:
    print(f'남은 기회 : {life}번')
    user_guess = input('알파벳 한 문자씩 입력하세요. : ').lower()
    
    if len(user_guess) == 1 and user_guess.isalpha():
        for i in range(len(answer)):
            if answer[i] == user_guess:
                guess_letters[i] = user_guess
        print(guess_letters)
        if "_" not in guess_letters:
            game_over = True
            print('성공하였습니다.')
        if user_guess not in answer:
            life = life - 1
            if life == 0:
                game_over = True
                print(f'실패!! 정답은 {answer}입니다')
    
    else:
        print('영문 알파벳 한 글자씩 넣어주세요.')