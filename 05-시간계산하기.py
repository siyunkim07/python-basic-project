# 1. 초(second)를 입력 받아서, 분과 초로 출력하는 프로그램을 코딩하라.
# 2. 예를 들어 2500 입력하면
# 3 결과를 '입력한 2500초는 x분 x초입니다.' 와 같이 출력한다.


result = int(input('초(second)를 입력하세요 : '))
print(result)

result1 = result // 60
result2 = result % 60
print(f'입력한 {result}초는 {result1}분 {result2}초 입니다.')