# List = [1, 2, 4, 6, 7, 9]
# key = 2
#
# def search(List, key):
#     left = -1
#     right = len(List)
#     while right > left + 1:
#         middle = left + right // 2
#         if List[middle] > key:
#             right = middle
#         else:
#             left = middle
#     return right
#
# print(search(List, key))

A = [1, 2, 3, 4]
key = 4

def LowerBound(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            right = middle
        else:
            left = middle
    return right

print(LowerBound(A, key))