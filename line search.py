list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
searchSymb = input('Введите искомый символ: ')
print(list.index(searchSymb))
def lineSearch(list, x):
	result = None
	for index, string in enumerate(list):
		print(index, string)
		if string == x:
			result = index
	return result
