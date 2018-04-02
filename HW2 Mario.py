# # Пирамида №1
# x=int(input("Введите высоту пирамиды: "))
# if x > 0:
#      for i in range(x):
#         print(' ' * (x-i-1) + '*' * (i*2+1))
# else:
#    print("Твоя принцесса в другом замке")

# №2
height=int(input("Введите высоту пирамиды: "))
while 0 == 0:
    if height > 0 and height <= 23:
        for i in range(height):
            print(' ' * (height-i-1) + '*' * (i+2))
        break
    elif height > 23:
        height = int(input("С такой высоты Марио разобьётся, введите число поменьше: ")
    else:
        height = int(input("Твоя принцесса в другом замке, попроуйте ещё раз: ")
