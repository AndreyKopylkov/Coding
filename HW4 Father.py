#coding=utf-8
fathers = {'Harold Abelson': 'Logo',
        'Kenneth Eugene Iverson': 'APL',
        'Andrei Alexandrescu': 'C++',
        'Alfred Vaino Aho': 'AWK',
        'Guido van Rossum': 'Python',
        'Jeremy Ashkenas': 'CoffeeScript',
        'Walter Bright': 'D',
        'John George Kemeny': 'Basic',
        'Peter Naur': 'Algol',
        'Don Syme': 'F#'
        }
choiceAction = input('Что вы хотите сделать? Введите Sorted или Search: ')
if choiceAction == 'Sorted':
        sortName = sorted(fathers.keys())
        for lang in sortName:
                print(lang, " - ", fathers[lang])
elif choiceAction == 'Search':
        searchName = input("Кого вы хотите найти? Введите имя: ")
        for name, value in fathers.items():
                if name == searchName:
                        print(searchName, 'участовал в разработке языка', fathers[name])
                        break
        else:
                print("Не удалось найти этого человека")
else:
        print('Попробуйте ещё раз, возможно вы ввели команду неправильно')
