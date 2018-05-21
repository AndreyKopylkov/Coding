list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']

search = input('Введите искомую букву: ')
print(list.index(search))

def lineSearch(list, x):
	result = None
	for index, string in enumerate(list):
		print(index, string)
		if string == x:
			result = index
	return result
