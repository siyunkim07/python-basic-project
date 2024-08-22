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
f = open("신발재고.txt", 'w', encoding='utf8')
for  i,j in stock.items():
    data = f'{i}:{j}\n'
    f.write(data)
f.close()
# stock = {}
# f = open("신발재고.txt", 'r', encoding='utf8')
# lines = f.readlines()
# for line in lines:
#     size,num = line.strip().split(':')
#     stock[size] = int(num)
#     print(stock)
# f.close()
