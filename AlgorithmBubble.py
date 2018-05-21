list = [8, 1, 2, 6, 0, 9, 23, 56, 100, 93, 82, 8, 42]
counter = 1
while counter < len(list):
     for i in range(len(list) - counter):
          if list[i] > list[i + 1]:
              list[i], list[i + 1] = list[i + 1], list[i]
     counter += 1
     print(list)
