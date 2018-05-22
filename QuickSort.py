list = [8, 1, 2, 6, 0, 9, 23, 56, 100, 93, 82, 8, 42]
def QuickSort(a):
    a = list
    if len(a) <= 1:
        return a
        print(a)
    else:
        q = (a)
        L = []
        M = []
        R = []
        for elem in a:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        print(a)
        return QuickSort(L) + M + QuickSort(R)
