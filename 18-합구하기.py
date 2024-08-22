# 사용자로 부터 두개의 숫자를 입력받는다.
# 두개의 숫자 사이의 모든 숫자의 합을 구하라
# 예를 들어, 첫번째 숫자가 132, 두번째 숫자가 150이다 132~ 150 사이의 모든 수의 합을 구한다.

# 합을 구해서 결과를 출력한다.
# 단 두개의 숫자는 하나의 input으로 입력받는다.


num1, num2 = input('숫자를 입력하세요 : ').split(' ')

num1 = int(num1)   
num2 = int(num2)

sum = 0
for i in range(num1, num2 + 1):
    sum = sum + i
print(sum)

