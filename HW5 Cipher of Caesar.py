message = input('Введите текст на русском языке для зашифровки: ').lower()
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
      'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
shift = int(input('Введите размер смещения: '))
new_mes = []
new_mes2 = ''
for i in message:
    if i not in alph:
             new_mes.append(i)
    else:
        new_mes.append(alph[alph.index(i) + shift])
for i in range(len(new_mes)):
    new_mes2 += new_mes[i]
print('Зашифрованное сообщение: ', new_mes2)
