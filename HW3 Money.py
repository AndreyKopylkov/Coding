kopeck = [50, 10, 5, 1]
money = [0, 0, 0, 0]
summ = int (input('Введите номинал вашей купюры: '))
print('Необходимо выдать:')
for i in range(len(kopeck)):
    while summ >= kopeck[i]:
        summ -= kopeck[i]
        money[i] += 1
    print(money[i], 'монеты по', kopeck[i], 'копейек')
