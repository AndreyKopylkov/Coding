message = input('Введите текст на русском языке для зашифровки: ').lower()
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
      'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
new_mes = []
new_mes2 = ''
for i in message:
    if i not in alph:
             new_mes.append(i)
    else:
        new_mes.append(alph[alph.index(i) + 3])
#with open('word.txt','w') as f:
#    for i in new_mes:
#        f.write(i)
#with open('word.txt','r') as f:
#    print('Зашифрованный текст:\n',f.read())
for i in range(len(new_mes)):
    new_mes2 += new_mes[i]
print(new_mes2)
