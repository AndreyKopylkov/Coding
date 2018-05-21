list = [8, 1, 2, 6, 0, 9, 23, 56, 100, 93, 82, 8, 42]
searchSymb = int(input('Введите искомый символ: '))
def search(List, key):
    left = -1
    right = len(List)
    while right > left + 1:
        middle = left + right // 2
        if List[middle] > key:
            right = middle
        else:
            left = middle
    return right
print('Номер вашего символа: ', search(list, searchSymb) - 1)
