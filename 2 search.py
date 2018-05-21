list = [1, 2, 4, 6, 7, 9]
searchSymb = int(input('Введите искомый символ: '))
def search(list, key):
    left = -1
    right = len(list)
    while right > left + 1:
        middle = left + right // 2
        if list[middle] > key:
            right = middle
        else:
            left = middle
    return right
print('Номер вашего символа: ', search(list, searchSymb) - 1)
