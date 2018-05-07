kopeck = [50, 10, 5, 1]
money = [0, 0, 0, 0]
summ = int (input('Введите номинал вашей купюры: '))
while summ >= 50:
    summ -=50
    money[0] += 1
while summ >= 10:
    summ -= 10
    money[1] += 1
while summ >= 5:
    summ -=5
    money[2] += 1
while summ >= 1:
    summ -= 1
    money[3] += 1
print('Необходимо выдать:')
for i in range(len(kopeck)):
    print(money[i], 'монеты по', kopeck[i], 'копейек')
