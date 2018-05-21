# def selection_sort(arrayToSort):
#     a = arrayToSort
#     for i in range(len(a)):
#         idxMin = i
#         for j in range(i+1, len(a)):
#             if a[j] < a[idxMin]:
#                 idxMin = j
#         tmp = a[idxMin]
#         a[idxMin] = a[i]
#         a[i] = tmp
#     return a
#
# ary = [0,3,5,1,2,3,5,4,2,314,43,24]
# print selection_sort(ary)


# def selectSort (arrayToSort):
#     a = arrayToSort
#     for i in range(len(a)):
#         idxMin = i
#         for j in range(i + 1, len(a)):
#             if a[j] < a[idxMin]:
#                 idxMin = j
#         tmp = a[idxMin]
#         a[idxMin] = a[i]
#         a[i] = tmp
#     return a
#
# ary = [0,3,5,24,2,123,53,64,85]
# print selectSort(ary)


def secetSort (arrayNumber):
    a = arrayNumber
    for i in range(len(a)):
        NumMin = i
        for j in range (i + 1, len(a)):
            if a[j] < a[NumMin]:
                NumMin = j
        SelectNumber = a[NumMin]
        a[NumMin] = a[i]
        a[i] = SelectNumber
    return a

array = [5,34,42,42,643,743,7,463,2]
print (secetSort(array))







